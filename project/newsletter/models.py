# coding: utf8
from django.db import models
from auf.django.references.models import Region
from project.auf_site_institutionnel.models import Actualite, Appel_Offre, Evenement, Publication, Bourse
from django import forms
from cms.models import CMSPlugin

# Create your models here.

class Newsletter(models.Model):
    status = models.CharField(max_length=1, default='3', null=False, blank=False, choices=(('1', 'En cours de redaction'), ('2', 'Propose a la publication'), ('3', 'Publie en Ligne'), ('4', 'A supprimer')))
    numero = models.IntegerField(max_length=11,default=0)
    date = models.DateField()
    bureau = models.ManyToManyField(Region)
    titre_dossier = models.CharField(max_length=255, null=True, blank=True, verbose_name='Titre')
    texte_dossier = models.TextField(null=True, blank=True)
    photo_dossier = models.ImageField(upload_to='planete', null=True, blank=True)
    lien_dossier = models.URLField(max_length=300, null=True, blank=True)
    appel = models.ManyToManyField(Appel_Offre, related_name='+', limit_choices_to={'status': 3}, verbose_name='Appels d\'offres', blank=True, null=True)
    actualite = models.ManyToManyField(Actualite, limit_choices_to={'status': 3}, verbose_name='Actualités universitaires', blank=True, null=True)
    evenement = models.ManyToManyField(Evenement, limit_choices_to={'status': 3}, verbose_name='Evénements', blank=True, null=True)
    publication = models.ManyToManyField(Publication, limit_choices_to={'status': 3}, verbose_name='Publication', blank=True, null=True)
    lien = models.EmailField(max_length=200, default='webmestre@auf.org')
    lien2 = models.URLField(max_length=250, default='http://www.auf.org')
    lienFace = models.URLField(max_length=250, default='http://www.facebook.com/aufinternational')
    abonne = models.IntegerField(max_length=11,default='1000')
    footer = models.TextField(default='Lettre electronique est une publication realisee par Agence universitaire de la Francophonie. AUF operateur direct de la Francophonie est un reseau mondial de 781 etablissements enseignement superieur et de recherche.')
    
class Abonne(models.Model):
    adresse = models.EmailField(max_length=75, verbose_name='Adresse')
    date = models.DateField(auto_now_add=True)
    bureau = models.ManyToManyField(Region)
    valide = models.BooleanField()
    
class Fil(models.Model):
    numero = models.IntegerField(max_length=11,default=0)
    bureau = models.ManyToManyField(Region)
    date = models.DateField()
    actualite = models.ManyToManyField(Actualite, limit_choices_to={'status': 3}, verbose_name='Choix des actualités', blank=True, null=True)
    evenement = models.ManyToManyField(Evenement, limit_choices_to={'status': 3}, verbose_name='Choix des événements', blank=True, null=True)
    footer = models.TextField(default='Copyright AUF 2013')  
    
    def __unicode__(self):
        return 'Fil N'+unicode(self.numero)
    
class Planete(models.Model):
    status = models.CharField(max_length=1, default='3', null=False, blank=False, choices=(('1', 'En cours de redaction'), ('2', 'Propose a la publication'), ('3', 'Publie en Ligne'), ('4', 'A supprimer')))
    numero = models.IntegerField(max_length=11,default=0)
    date = models.DateField()
    titre_dossier = models.CharField(max_length=255, null=False, blank=False, verbose_name='Titre')
    texte_dossier = models.TextField(null=False, blank=False)
    photo_dossier = models.ImageField(upload_to='planete', null=True, blank=True)
    lien_dossier = models.URLField(max_length=300, null=True, blank=True)
    appel_planete = models.ManyToManyField(Appel_Offre, limit_choices_to={'status': 3}, verbose_name='Appels d\'offres', blank=True, null=True)
    bourse_planete = models.ManyToManyField(Bourse, limit_choices_to={'status': 3}, verbose_name='Bourses', blank=True, null=True)
    evenement_planete = models.ManyToManyField(Evenement, limit_choices_to={'status': 3}, verbose_name='Evénements', blank=True, null=True)
    fil_planete = models.ForeignKey(Fil, verbose_name='Fil d\'Actualités', blank=False, null=False)
    footer = models.TextField(default='Lettre electronique est une publication realisee par Agence universitaire de la Francophonie. AUF operateur direct de la Francophonie est un reseau mondial de 781 etablissements enseignement superieur et de recherche.')

class ProjetPlanete(models.Model):
    planete = models.ForeignKey(Planete, related_name='projets')
    titre_projet = models.CharField(max_length=255, null=False, blank=False, verbose_name='Titre')
    texte_projet = models.TextField(null=False, blank=False)
    photo_projet = models.ImageField(upload_to='planete', null=True, blank=True)
    lien_projet = models.URLField(max_length=300)
    ordre_projet = models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.titre_projet
        
class MembrePlanete(models.Model):
    planete = models.ForeignKey(Planete, related_name='membres')
    titre_membre = models.CharField(max_length=255, null=False, blank=False, verbose_name='Titre')
    texte_membre = models.TextField(null=False, blank=False)
    photo_membre = models.ImageField(upload_to='planete', null=True, blank=True)
    lien_membre = models.URLField(max_length=300)
    ordre_membre = models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.titre_membre
        
class Breve(models.Model):
    numero = models.IntegerField(max_length=11,default=0)
    date = models.DateField()
    texte_intro = models.TextField(blank=True)
    texte_rh = models.TextField(blank=True)
    texte_ari = models.TextField(blank=True)
    texte_agenda = models.TextField(blank=True)
    texte_mission = models.TextField(blank=True)
    texte_arrive = models.TextField(blank=True)
    texte_diver = models.TextField(blank=True, verbose_name='Réunions')
    texte_autre = models.TextField(blank=True, verbose_name='Autres informations importantes')
    footer = models.TextField(verbose_name='Texte pied de page', default='Les brèves des services centraux sont une publication réalisée par l\'Agence universitaire de la Francophonie. L\'AUF, opérateur de la Francophonie, est un réseau mondial de 800 établissements d\'enseignement supérieur et de recherche.')

class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ('adresse',)
        
    def clean(self):
        cleaned_data = self.cleaned_data

        if Abonne.objects.filter(adresse=cleaned_data.get("adresse")):
            raise forms.ValidationError("Vous êtes déja inscrit à la lettre d\'information")

        return cleaned_data
        
class DesinscireForm(forms.Form):
    adresse = forms.EmailField(label="", max_length=75)
    
    def clean(self):
        cleaned_data = self.cleaned_data

        if not Abonne.objects.filter(adresse=cleaned_data.get("adresse")):
            raise forms.ValidationError("Vous êtes pas inscrit à la lettre d\'information")

        return cleaned_data

class VideoPlugin(CMSPlugin):
    titre = models.CharField(max_length=250)
    video = models.TextField(null=True, blank=True, verbose_name='Code de la vidéo')
    description = models.TextField(null=True, blank=True, verbose_name='Description de la vidéo')
    
    def __unicode__(self):
        return self.titre

    def copy_relations(self, oldinstance):
        self.sections = oldinstance.sections.all()
