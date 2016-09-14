# -=- encoding: utf-8 -=-
import random
import string
import datetime

from django.db import models
from django.contrib.auth.models import User

import auf.django.references.models as ref


RESPONSABLE_ETABLISSEMENT = u'r'
RESPONSABLE_COMMUNICATION = u'c'
RESPONSABLE_RELATIONS_INTERNATIONALES = u'i'

ETABLISSEMENT_CHOIX = (
    (u"ESR", u"Établissement d'enseignement supérieur et de recherche"),
    (u"CIR", u"Centre ou institution de recherche"),
    (u"RES", u"Réseaux"),
)
RESPONSABLE_CHOIX = (
    (RESPONSABLE_ETABLISSEMENT, u"Responsable d'établissement"),
    (RESPONSABLE_COMMUNICATION, u"Communication"),
    (RESPONSABLE_RELATIONS_INTERNATIONALES, u"Relations internationales"),
)


class EtablissementAbstrait(ref.EtablissementBase):
    courriel = models.CharField(max_length=128,
                                verbose_name=u"Courriel général")
    nombre = models.IntegerField(null=True)
    chiffres_cles = models.TextField(verbose_name=u"Chiffres clés", blank=True)
    publication_papier = models.BooleanField(default=True)
    publication_electronique = models.BooleanField(default=True)

    class Meta:
        abstract = True
        verbose_name = u'Établissement'
        verbose_name_plural = u'Établissements'

    def __unicode__(self):
        return u"%s" % self.nom


def make_diff(obj):
    def compare_attr(value1, value2):
        def strip_end_slash(value):
            return value[:-1] if value and isinstance(value, unicode) and value[-1] == u"/" else value

        # URLField normalise les URL à la validation, et rajoute un slash à la fin
        # si il n'y en pas déjà un. Ce n'est pas considéré comme une
        # modification du champ.
        return strip_end_slash(value1) == strip_end_slash(value2)

    diff = {}
    if obj.id:
        fields_to_ignore = obj.ignore_in_diff
        ancien = obj.ancien()
        for f in obj._meta.fields:
            if not f.name == 'id' and f.name not in fields_to_ignore:
                try:
                    if not ancien:
                        diff[f.name] = ""
                    elif not compare_attr(getattr(ancien, f.name),
                                          getattr(obj, f.name)):
                        diff[f.name] = getattr(ancien, f.name)
                except AttributeError:
                    pass
    return diff


class Diffable(object):
    @property
    def diff(self):
        if not hasattr(self, '_diff'):
            self._diff = make_diff(self)
        return self._diff


class Etablissement(EtablissementAbstrait):
    pass


class EtablissementModification(EtablissementAbstrait, Diffable):
    etablissement = models.OneToOneField(
        Etablissement, null=True, related_name='modification')
    validation_etablissement = models.BooleanField(default=False,
                                                   verbose_name=u"Validé par l'établissement")
    validation_sai = models.BooleanField(default=False,
                                         verbose_name=u"Validé par le SAI")
    validation_com = models.BooleanField(default=False,
                                         verbose_name=u"Validé par COM")
    date_validation_etablissement = models.DateField(null=True)
    date_validation_sai = models.DateField(null=True)
    date_validation_com = models.DateField(null=True)

    a_valider_sai = models.BooleanField(
        default=False, verbose_name=u"À valider par le SAI")
    a_valider_com = models.BooleanField(
        default=False, verbose_name=u"À valider par le COM")

    export_gde_sai = models.BooleanField(
        default=False, verbose_name=u"Exporté vers GDE par SAI")
    export_gde_com = models.BooleanField(
        default=False, verbose_name=u"Exporté vers GDE par COM")

    champs_com = ('historique', 'description', 'chiffres_cles',
                  'publication_papier', 'publication_electronique')

    ignore_in_diff = ()

    def code_region(self):
        return self.region.code

    def ancien(self):
        return self.etablissement

    def __init__(self, *args, **kwargs):
        super(EtablissementModification, self).__init__(*args, **kwargs)
        self._original_state = dict(self.__dict__)

    def set_flags_a_valider(self):
        self.validation_com = True
        self.validation_sai = True
        for field_name in self.diff.keys():
            if field_name in self.champs_com:
                self.a_valider_com = True
                self.validation_com = False
            else:
                self.validation_sai = False
                self.a_valider_sai = True

        for responsable in self.responsablemodification_set.all():
            responsable.set_flags_a_valider(self)

    def save(self, *args, **kwargs):
        if self._original_state['validation_sai'] == False and \
                self.validation_sai == True:
            self.date_validation_sai = datetime.date.today()

        if self._original_state['validation_com'] == False and\
                self.validation_com == True:
            self.date_validation_com = datetime.date.today()
        print "validé sai" if self.validation_sai else "non validé SAI"

        super(EtablissementModification, self).save(*args, **kwargs)

    def get_responsables_set(self):
        return Responsable.objects.filter(etablissement=self.etablissement_id)

    def get_responsables_modification_set(self):
        return ResponsableModification.objects.filter(etablissement=self)

    def get_responsables_pha(self):
        return self.get_responsables_set().filter(type=RESPONSABLE_ETABLISSEMENT)

    def get_responsables_com(self):
        return self.get_responsables_set().filter(type=RESPONSABLE_COMMUNICATION)

    def get_responsables_modification_pha(self):
        return self.get_responsables_modification_set().filter(type=RESPONSABLE_ETABLISSEMENT)

    def get_responsables_modification_com(self):
        return self.get_responsables_modification_set().filter(type=RESPONSABLE_COMMUNICATION)

    validation_etablissement.validation_sai_com_filter = True


class ResponsableAbstrait(models.Model):
    genre = models.CharField(max_length=1, blank=True)
    nom = models.CharField(max_length=128, blank=True)
    prenom = models.CharField(
        max_length=128, blank=True, verbose_name=u"Prénom")
    courriel = models.CharField(max_length=128)
    type = models.CharField(max_length=1, choices=RESPONSABLE_CHOIX)
    modification_date = models.DateTimeField(auto_now=True, null=True,
                                             verbose_name=u"Date de modification")
    modification_par = models.CharField(max_length=100, null=True,
                                        verbose_name=u"Modifié par")

    salutation = models.CharField(max_length=64, blank=True, default=u"")
    fonction = models.CharField(max_length=128, blank=True, default=u"")
    sousfonction = models.CharField(
        max_length=64, blank=True, default=u"", verbose_name=u"Sous-fonction")

    class Meta:
        abstract = True
        verbose_name = u"Responsable"

    def __unicode__(self):
        return "%s %s" % (self.prenom, self.nom)


class Responsable(ResponsableAbstrait):
    etablissement = models.ForeignKey(Etablissement)


class ResponsableModification(ResponsableAbstrait, Diffable):
    etablissement = models.ForeignKey(EtablissementModification)
    responsable = models.OneToOneField(Responsable, null=True)

    ignore_in_diff = ("etablissement", "modification_date", "modification_par")

    def ancien(self):
        return self.responsable

    def __init__(self, *args, **kwargs):
        super(ResponsableModification, self).__init__(*args, **kwargs)

    def set_flags_a_valider(self, etablissement):
        if not self.id or self.diff:
            if self.type == RESPONSABLE_COMMUNICATION:
                etablissement.a_valider_com = True
                etablissement.validation_com = False
            else:
                etablissement.a_valider_sai = True
                etablissement.validation_sai = False

    def save(self, *args, **kwargs):
        self.nom = self.nom.upper()
        super(ResponsableModification, self).save(*args, **kwargs)


class Acces(models.Model):
    etablissement = models.ForeignKey(Etablissement)
    token = models.CharField(max_length=128, unique=True, null=False)
    active = models.NullBooleanField()

    token_charset = "abcdefghiklmnopqrstuvwxyz01234567890"

    class Meta:
        verbose_name = u"Code d'accès"
        verbose_name_plural = u"Codes d'accès"

    def __unicode__(self):
        return u"%s" % self.etablissement

    def generer_token(self, size=32):
        self.token = ''.join(random.choice(string.letters + string.digits)
                             for i in xrange(size))


class Courriel(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True,
                                         verbose_name=u"Date de création")
    user_creation = models.ForeignKey(User,
                                      verbose_name=u"Créé par")
    sujet = models.CharField(max_length=255)
    contenu = models.TextField()

    class Meta:
        verbose_name = u"Courriel"
        verbose_name_plural = u"Courriels"

    def __unicode__(self):
        return u"%s - %s" % (self.date_creation, self.sujet)


class CourrielLog(models.Model):
    courriel = models.ForeignKey(Courriel)
    etablissement = models.ForeignKey(Etablissement)
    adresse_courriel = models.CharField(max_length=128, null=True)
    envoye = models.BooleanField(default=False, db_index=True)
    envoye_le = models.DateTimeField(null=True)
