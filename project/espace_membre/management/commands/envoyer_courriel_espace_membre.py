# -*- encoding: utf-8 -*-
from optparse import make_option
import time

from django.core.management.base import BaseCommand, CommandError
from django.db.models.query_utils import Q
from django.template import Context, Template
from django.core.mail import EmailMessage
from django.db import transaction
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

import smtplib
import datetime

from project.espace_membre import models as espace_membre


class Command(BaseCommand):

    """
    Commande pour envoyer aux membres un courriel leur demandant, ou leur rappelant
    de mettre à jour leurs données dans l'espace membre.

    Le paramètre --mode permet de choisir le type d'envoi:
    * initial: envoi à tous les responsables de tous les établissements membres qui ont
    une adresse de courriel
    * rappel: idem à initial moins tous ceux qui ont validé leurs données dans l'espace
    membre

    Dans les deux cas, un log est tenu qui enregistre chaque courriel effectivement 
    envoyé. Cette commande peut donc être exécutée plusieurs fois avec les mêmes
    paramètres sans risque d'envoyer le même courriel aux mêmes personnes.
    """
    help = u"Procède à l'envoi du courriel demandant aux membres de remplir le formulaire de l'annuaire"
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

    @transaction.commit_manually()
    def handle(self, *args, **options):
        if not options['email_id']:
            raise CommandError(
                u"Vous devez specifier le ID du courriel a envoyer avec l'argument --id")

        try:
            email = espace_membre.Courriel.objects.get(id=options['email_id'])
        except espace_membre.Courriel.DoesNotExist:
            raise CommandError("Le courriel (id=%s) n'existe pas."
                               % options['email_id'])

        site = Site.objects.get(id=1)
        try:
            #            responsables_queryset = espace_membre.Responsable.objects.filter(type=espace_membre.RESPONSABLE_ETABLISSEMENT)\
            #                .exclude(courriel='').exclude(courriel__isnull=True)\
            #                .exclude(etablissement__actif__exact=False)\
            #                .select_related('etablissement')
            #            if options['mode_envoi'] == 'rappel':
            #                responsables_queryset = responsables_queryset.exclude(etablissement__modification__validation_etablissement=True)

            etablissements_queryset = espace_membre.Etablissement.objects\
                .filter(actif=True, membre=True)
            if options['mode_envoi'] == 'rappel':
                etablissements_queryset = etablissements_queryset\
                    .exclude(modification__validation_etablissement=True)

            for etablissement in etablissements_queryset:
                # de préférence on envoie au PHA
                responsable_pha = etablissement.responsable_set\
                    .filter(type=espace_membre.RESPONSABLE_ETABLISSEMENT)\
                    .exclude(courriel='').exclude(courriel__isnull=True)
                if len(responsable_pha):
                    adresse_courriel = responsable_pha[0].courriel
                else:
                    # mais s'il n'a pas d'adresse, on envoie à l'adresse
                    # générale
                    if etablissement.courriel:
                        adresse_courriel = etablissement.courriel
                    else:
                        # en dernier recours on cherche l'adresse du
                        # responsable comm
                        responsable_com = etablissement.responsable_set\
                            .filter(type=espace_membre.RESPONSABLE_COMMUNICATION)\
                            .exclude(courriel='').exclude(courriel__isnull=True)
                        if len(responsable_com):
                            adresse_courriel = responsable_com[0].courriel
                        else:
                            # on n'a trouvé aucune adresse pour cet
                            # établissement
                            continue
                # on vérifie qu'on n'a pas déjà envoyé ce courriel à
                # cet établissement et à cette adresse
                log = espace_membre.CourrielLog.objects.filter(etablissement=etablissement,
                                                               envoye=True, courriel=email, adresse_courriel=adresse_courriel)
                if log.count() > 0:
                    continue

                tokens = espace_membre.Acces.objects \
                    .filter(etablissement=etablissement, active=True)

                url = 'http://%s%s' % (site.domain,
                                       reverse('espace_membre_connexion', kwargs={'token': tokens[0].token}))
                modele_corps = Template(email.contenu)
                contexte_corps = Context({
                    "nom_etablissement": etablissement.nom,
                    "lien": url  # '<a href="%s">%s</a>' % (url, url)
                })
                corps = modele_corps.render(contexte_corps)
                message = EmailMessage(email.sujet,
                                       corps,
                                       # adresse de retour
                                       settings.ESPACE_MEMBRE_SENDER,
                                       # adresse du destinataire
                                       [adresse_courriel],
                                       # selon les conseils de google
                                       headers={'precedence': 'bulk'}
                                       )
                try:
                    # Attention en DEV, devrait simplement écrire le courriel
                    # dans la console, cf. paramètre EMAIL_BACKEND dans conf.py
                    # En PROD, supprimer EMAIL_BACKEND (ce qui fera retomber sur le défaut
                    # qui est d'envoyer par SMTP). Même chose en TEST, mais attention
                    # car les adresses qui sont dans la base seront utilisées:
                    # modifier les données pour y mettre des adresses de test plutôt que
                    # les vraies
                    message.content_subtype = "html"
                    message.send()
                    log = espace_membre.CourrielLog()
                    log.etablissement_id = etablissement.id
                    log.courriel = email
                    log.adresse_courriel = adresse_courriel
                    log.envoye_le = datetime.datetime.today()
                    log.envoye = True
                    log.save()
                    transaction.commit()
                    time.sleep(2)
                except smtplib.SMTPException as e:
                    self.stdout.write(
                        u"Erreur lors de l'envoi pour etablissement ID: %s\n" % etablissement.id)
                    self.stdout.write(e.__str__())
        except:
            transaction.rollback()
            raise

        # nécessaire dans le cas où rien n'est envoyé, à cause du décorateur
        # commit_manually
        transaction.commit()
