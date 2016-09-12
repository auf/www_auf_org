# -*- encoding: utf-8 -*-
from optparse import make_option
import time

from django.core.management.base import BaseCommand, CommandError
from django.template import Context, Template
from django.core.mail import EmailMessage
from django.db import transaction
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

import smtplib
import datetime

from project.espace_membre import models as espace_membre


def get_courriel_responsable(etablissement, type_responsable):
    responsables = etablissement.responsable_set\
                    .filter(type=type_responsable)\
                    .exclude(courriel='').exclude(courriel__isnull=True)
    try:
        return responsables[0].courriel
    except IndexError:
        return None


def get_cc(to, courriel_responsable_com, courriel_relations_internationales):
    cc = []
    if (courriel_responsable_com and
            to != courriel_responsable_com):
        cc.append(courriel_responsable_com)
    if courriel_relations_internationales:
        cc.append(courriel_relations_internationales)
    return cc


class Command(BaseCommand):

    """
    Commande pour envoyer aux membres un courriel leur demandant, ou leur
    rappelant de mettre à jour leurs données dans l'espace membre.

    Le paramètre --mode permet de choisir le type d'envoi:
    * initial: envoi à tous les responsables de tous les établissements membres
    qui ont une adresse de courriel
    * rappel: idem à initial moins tous ceux qui ont validé leurs données dans
    l'espace membre

    Dans les deux cas, un log est tenu qui enregistre chaque courriel
    effectivement envoyé. Cette commande peut donc être exécutée plusieurs fois
    avec les mêmes paramètres sans risque d'envoyer le même courriel aux mêmes
    personnes.
    """
    help = u"Procède à l'envoi du courriel demandant aux membres de remplir " \
           u"le formulaire de l'annuaire"
    option_list = BaseCommand.option_list + (
        make_option('--id',
                    action='store',
                    dest='email_id',
                    default=False,
                    help=u"Le ID du courriel à utiliser"),
        make_option('--mode',
                    action='store',
                    dest='mode_envoi',
                    default=False,
                    help=u"Mode d'envoi: `initial` ou `rappel`"),
    )

    # noinspection PyDeprecation
    @transaction.commit_manually()
    def handle(self, *args, **options):
        if not options['email_id']:
            raise CommandError(u"Vous devez specifier le ID du courriel a "
                               u"envoyer avec l'argument --id")
        try:
            email = espace_membre.Courriel.objects.get(id=options['email_id'])
        except espace_membre.Courriel.DoesNotExist:
            raise CommandError("Le courriel (id=%s) n'existe pas."
                               % options['email_id'])

        site = Site.objects.get(id=1)
        try:
            etablissements_queryset = espace_membre.Etablissement.objects\
                .filter(actif=True, membre=True)
            if options['mode_envoi'] == 'rappel':
                etablissements_queryset = etablissements_queryset\
                    .exclude(modification__validation_etablissement=True)

            for etablissement in etablissements_queryset:
                # de préférence on envoie au PHA
                courriel_responsable_pha = get_courriel_responsable(
                    etablissement, espace_membre.RESPONSABLE_ETABLISSEMENT)
                etablissement_courriel = etablissement.courriel
                courriel_responsable_com = get_courriel_responsable(
                            etablissement,
                            espace_membre.RESPONSABLE_COMMUNICATION)
                to = (courriel_responsable_pha or
                      etablissement_courriel or
                      courriel_responsable_com)
                if not to:
                    continue
                # on vérifie qu'on n'a pas déjà envoyé ce courriel à
                # cet établissement et à cette adresse
                if espace_membre.CourrielLog.objects.filter(
                        etablissement=etablissement,
                        envoye=True, courriel=email,
                        adresse_courriel=to).count() > 0:
                    continue

                tokens = espace_membre.Acces.objects \
                    .filter(etablissement=etablissement, active=True)
                url = 'https://{}{}'.format(
                    site.domain, reverse('espace_membre_connexion',
                                         kwargs={'token': tokens[0].token}))
                modele_corps = Template(email.contenu)
                contexte_corps = Context({
                    "nom_etablissement": etablissement.nom,
                    "lien": url  # '<a href="%s">%s</a>' % (url, url)
                })
                corps = modele_corps.render(contexte_corps)

                courriel_relations_internationales = get_courriel_responsable(
                    etablissement,
                    espace_membre.RESPONSABLE_RELATIONS_INTERNATIONALES)
                cc = get_cc(to, courriel_responsable_com,
                            courriel_relations_internationales)
                message = EmailMessage(email.sujet,
                                       corps,
                                       # adresse de retour
                                       settings.ESPACE_MEMBRE_SENDER,
                                       # adresse du destinataire
                                       [to], cc=cc,
                                       # selon les conseils de google
                                       headers={'precedence': 'bulk'}
                                       )
                try:
                    # Attention en DEV, devrait simplement écrire le courriel
                    # dans la console, cf. paramètre EMAIL_BACKEND dans conf.py
                    # En PROD, supprimer EMAIL_BACKEND (ce qui fera retomber sur
                    #  le défaut qui est d'envoyer par SMTP). Même chose en
                    # TEST, mais attention car les adresses qui sont dans la
                    # base seront utilisées: modifier les données pour y mettre
                    # des adresses de test plutôt que les vraies
                    message.content_subtype = "html"
                    message.send()
                    log = espace_membre.CourrielLog()
                    log.etablissement_id = etablissement.id
                    log.courriel = email
                    log.adresse_courriel = to
                    log.envoye_le = datetime.datetime.today()
                    log.envoye = True
                    log.save()
                    transaction.commit()
                    # time.sleep(2)
                except smtplib.SMTPException as e:
                    err_message = u"Erreur lors de l'envoi pour etablissement "\
                        u"ID: {}}\n"
                    self.stdout.write(err_message.format(etablissement.id))
                    self.stdout.write(e.__str__())
        except:
            transaction.rollback()
            raise

        # nécessaire dans le cas où rien n'est envoyé, à cause du décorateur
        # commit_manually
        transaction.commit()
