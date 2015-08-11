# coding: utf8
import os

from django.db import models
from django.db.models.signals import post_init
from django.contrib.auth.models import User
from django.conf import settings

from cms.models.fields import PlaceholderField
from cms.models.pluginmodel import CMSPlugin

from auf.django.references.models import Employe, Region, Service

from project.cmsplugin_modellist.lib.choices import DynamicTemplateChoices

TEMPLATE_PATH = os.path.join("auf_site_institutionnel/employe", "layouts")

STATUTS = (
    ('1', 'En cours de rédaction'),
    ('2', 'Proposé à la publication'),
    ('6', 'Publié sur les sites régionaux'),
    ('3', 'Publié sur les sites régionaux et international'),
    ('5', 'Publié sur le site international'),
    ('4', 'Dépublié')
)


def association_employe_avec_django_user(sender, **kwargs):
    """
    Lorsqu'on manipule un user Django, on essaye de lui définir une
    propriété 'employe' de l'objet Employe du datamaster qui le représente.
    Si le compte est local par exemple non AUF, la propriété employe est fixée à None.
    """
    instance = kwargs.get('instance')

    if instance.id is None:
        return

    try:
        employe = Employe.objects.get(courriel=instance.email)
    except:
        if settings.DEBUG:
            "don't exist"
        employe = None

    setattr(instance, 'employe', employe)

post_init.connect(association_employe_avec_django_user, sender=User)


class Personna(models.Model):
    nom = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.nom


class Bourse(models.Model):
    bureau = models.ManyToManyField(
        Region, blank=True, null=True, related_name="bourse_bureau")
    personna = models.ManyToManyField(Personna)
    titre = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    texte = models.TextField(null=True, blank=True)
    cmstexte = PlaceholderField('texte')
    image = models.ImageField(upload_to='bourse', null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    date_fin2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=(
            ('1',
             '1 Moi avant le début des manifestations'),
            ('2',
             '2 Mois avant le début des manifestations'),
            ('3',
             '3 Mois avant le début des manifestations'),
            ('4',
             '4 Mois avant le début des manifestations'),
            ('5',
             '5 Mois avant le début des manifestations'),
            ('6',
             'Permanent')))
    date_pub = models.DateTimeField('date de creation')
    date_mod = models.DateTimeField(
        'date de derniere modification', auto_now_add=True)
    status = models.CharField(
        max_length=1, default='3', null=False, blank=False, choices=STATUTS)

    class Meta:
        ordering = ('-date_pub',)

    def __unicode__(self):
        return self.titre

    def get_absolute_url(self):
        return "/allocations/%s/" % self.slug

    def get_absolute_url_region(self):
        return "/allocations-regionales/%s/" % self.slug

    def save(self, *args, **kwargs):
        object = super(Bourse, self).save(*args, **kwargs)
        from cms.api import add_plugin
        if self.cmstexte.cmsplugin_set.count() == 0:
            add_plugin(self.cmstexte, "TextPlugin", "fr",
                       body="Double-cliquez ici pour ajouter votre texte")
        return object


class Actualite(models.Model):
    bureau = models.ManyToManyField(
        Region, blank=True, null=True, related_name="actualite_bureau")
    personna = models.ManyToManyField(Personna)
    titre = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    cmstexte = PlaceholderField('texte')
    texte = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='actualite')
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    date_pub = models.DateField('date')
    date_mod = models.DateTimeField(
        'date de derniere modification', auto_now_add=True)
    status = models.CharField(
        max_length=1, null=False, default='3', blank=False, choices=STATUTS)

    class Meta:
        ordering = ('-date_pub',)

    def __unicode__(self):
        return self.titre

    def get_absolute_url(self):
        return "/actualites/%s/" % self.slug

    def get_absolute_url_region(self):
        return "/actualites-regionales/%s/" % self.slug

    def save(self, *args, **kwargs):
        object = super(Actualite, self).save(*args, **kwargs)
        from cms.api import add_plugin
        if self.cmstexte.cmsplugin_set.count() == 0:
            add_plugin(self.cmstexte, "TextPlugin", "fr",
                       body="Double-cliquez ici pour ajouter votre texte")
        return object


class Veille(models.Model):
    bureau = models.ManyToManyField(
        Region, blank=True, null=True, related_name="veille_bureau")
    personna = models.ManyToManyField(Personna)
    titre = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    texte = models.TextField(null=True, blank=True)
    cmstexte = PlaceholderField('texte')
    image = models.ImageField(null=True, blank=True, upload_to='actualite')
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    date_pub = models.DateField('date')
    date_mod = models.DateTimeField(
        'date de derniere modification', auto_now_add=True)
    status = models.CharField(
        max_length=1, null=False, default='3', blank=False, choices=STATUTS)

    class Meta:
        ordering = ('-date_pub',)

    def __unicode__(self):
        return self.titre

    def get_absolute_url(self):
        return "/veille/%s/" % self.slug

    def get_absolute_url_region(self):
        return "/veille-regionale/%s/" % self.slug


class Appel_Offre(models.Model):
    bureau = models.ManyToManyField(
        Region, blank=True, null=True, related_name="appel_offre_bureau")
    auf = models.BooleanField(
        "Cet appel d'offre est un appel d'offre AUF (et non partenaire)",
        default="True")
    personna = models.ManyToManyField(Personna)
    titre = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    texte = models.TextField(null=True, blank=True)
    cmstexte = PlaceholderField('texte')
    image = models.ImageField(null=True, blank=True, upload_to='appel_offre')
    date_fin = models.DateField(null=True, blank=True)
    date_fin2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=(
            ('1',
             '1 Moi avant le début des manifestations'),
            ('2',
             '2 Mois avant le début des manifestations'),
            ('3',
             '3 Mois avant le début des manifestations'),
            ('4',
             '4 Mois avant le début des manifestations'),
            ('5',
             '5 Mois avant le début des manifestations'),
            ('6',
             'Permanent')))
    date_pub = models.DateTimeField('date de creation', auto_now_add=True)
    date_mod = models.DateTimeField(
        'date de derniere modification', auto_now=True)
    status = models.CharField(
        max_length=1, default='3', null=False, blank=False, choices=STATUTS)

    class Meta:
        ordering = ('-date_pub',)

    def __unicode__(self):
        return self.titre

    def get_absolute_url(self):
        return "/appels-offre/%s/" % self.slug

    def get_absolute_url_region(self):
        return "/appels-offre-regionales/%s/" % self.slug

    def save(self, *args, **kwargs):
        object = super(Appel_Offre, self).save(*args, **kwargs)
        from cms.api import add_plugin
        if self.cmstexte.cmsplugin_set.count() == 0:
            add_plugin(self.cmstexte, "TextPlugin", "fr",
                       body="Double-cliquez ici pour ajouter votre texte")
        return object


class Evenement(models.Model):
    bureau = models.ManyToManyField(
        Region, blank=True, null=True, related_name="evenement_bureau")
    titre = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    texte = models.TextField(null=True, blank=True)
    cmstexte = PlaceholderField('texte')
    image = models.ImageField(null=True, blank=True, upload_to='evenement')
    lieu = models.CharField(max_length=200, null=True, blank=True)
    detail_horaire = models.TextField(null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    date_pub = models.DateTimeField('date de creation', auto_now=True)
    date_mod = models.DateTimeField(
        'date de derniere modification', auto_now_add=True)
    status = models.CharField(
        max_length=1, default='3', null=False, blank=False, choices=STATUTS)

    class Meta:
        ordering = ('-date_debut',)

    def __unicode__(self):
        return self.titre

    def get_absolute_url(self):
        return "/evenements/%s/" % self.slug

    def get_absolute_url_region(self):
        return "/evenements-regionales/%s/" % self.slug

    def save(self, *args, **kwargs):
        object = super(Evenement, self).save(*args, **kwargs)
        from cms.api import add_plugin
        if self.cmstexte.cmsplugin_set.count() == 0:
            add_plugin(self.cmstexte, "TextPlugin", "fr",
                       body="Double-cliquez ici pour ajouter votre texte")
        return object


class Comares(models.Model):
    bureau = models.ManyToManyField(
        Region, blank=True, null=True, related_name="comares_bureau")
    titre = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    texte = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='actualite')
    date_pub = models.DateField('date')
    date_mod = models.DateTimeField(
        'date de derniere modification', auto_now_add=True)
    status = models.CharField(
        max_length=1, default='3', null=False, blank=False, choices=STATUTS)

    class Meta:
        ordering = ('-date_pub',)

    def __unicode__(self):
        return self.titre

    def get_absolute_url(self):
        return "/comares/%s/" % self.slug


class Publication(models.Model):
    bureau = models.ManyToManyField(
        Region, blank=True, null=True, related_name="publication_bureau")
    titre = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    texte = models.TextField(null=True, blank=True)
    cmstexte = PlaceholderField('texte')
    docu = models.FileField(null=True, blank=True, upload_to='publication')
    image = models.ImageField(null=True, blank=True, upload_to='publication')
    date_pub = models.DateField('date')
    date_mod = models.DateTimeField(
        'date de derniere modification', auto_now_add=True)
    status = models.CharField(
        max_length=1, default='3', null=False, blank=False, choices=STATUTS)

    class Meta:
        ordering = ('-date_pub',)

    def __unicode__(self):
        return self.titre

    def get_absolute_url(self):
        return "/publications/%s/" % self.slug

    def get_absolute_url_region(self):
        return "/publications-regionales/%s/" % self.slug

    def save(self, *args, **kwargs):
        object = super(Publication, self).save(*args, **kwargs)
        from cms.api import add_plugin
        if self.cmstexte.cmsplugin_set.count() == 0:
            add_plugin(self.cmstexte, "TextPlugin", "fr",
                       body="Double-cliquez ici pour ajouter votre texte")
        return object


class Partenaire(models.Model):
    type = models.CharField(
        max_length=1,
        choices=(
            ('1',
             'Etats et gouvernements'),
            ('2',
             'Organisations internationales'),
            ('3',
             'Cooperation décentralisee'),
            ('4',
             'Institutions universitaires et scientifiques'),
            ('5',
             'Acteurs economiques')))
    nom = models.TextField()
    objet = models.TextField()
    BUDGET = models.CharField(max_length=200)
    periode = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='partenaires')
    site = models.URLField(max_length=200)
    date_pub = models.DateTimeField('date de creation', auto_now=True)
    date_mod = models.DateTimeField(
        'date de derniere modification', auto_now_add=True)

    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
        return "/partenaire/%s/" % self.slug


class Responsable(models.Model):
    UO_Idx = models.AutoField(primary_key=True)
    UO_Desc_fr = models.CharField(max_length=255)
    UPR_POS_Idx = models.IntegerField()
    POS_Title_fr = models.CharField(max_length=255)
    User_Emp_Nb = models.CharField(max_length=16)
    User_Last_Name = models.CharField(max_length=50)
    User_First_Name = models.CharField(max_length=50)
    actif = models.BooleanField()

    class Meta:
        db_table = "ref_responsable"
        managed = False

    def __unicode__(self):
        return self.POS_Title_fr


class EmployePlugin(CMSPlugin):
    responsable = models.ForeignKey(
        Responsable, related_name="employe_plugin_responsable", null=True, blank=True)
    service = models.ForeignKey(
        Service, related_name="employe_plugin_service", null=True, blank=True)
    # FIXME
    fonction = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=set(
            ((e.fonction,
              e.fonction) for e in Employe.objects.filter(
                actif=True))))
    region = models.ForeignKey(
        Region, related_name="employe_plugin_region", null=True, blank=True)
    layout_template = models.CharField(
        "Template utilisé pour l'affichage",
        choices=DynamicTemplateChoices(
            path=TEMPLATE_PATH,
            include='.html',
            exclude='default'),
        max_length=256,
        help_text="""Utiliser le template pour afficher le contenu de la liste""")


class ImplantationPlugin(CMSPlugin):
    region = models.ForeignKey(
        Region,
        related_name="implantation_plugin_region",
        null=True,
        blank=True)
