# -*- coding: utf-8 -*-
from django.db import models
from auf.django.references.models import Region

class Actualite(models.Model):
    bureau = models.ManyToManyField(Region)
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    resume = models.TextField(null=True, blank=True)
    texte = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='actualite')
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    date_pub = models.DateField('date')
    date_mod = models.DateTimeField('date de derniere modification', auto_now_add=True)
    une = models.BooleanField('Garder cette actualité en haut de liste')
    status = models.CharField(max_length=1, null=False, default='3', blank=False, choices=(('1', 'En cours de redaction'), ('2', 'Propose a la publication'), ('3', 'Publie en Ligne'), ('4', 'A supprimer')))
    
    class Meta:
        ordering = ('-date_pub',)
        db_table = 'auf_site_institutionnel_actualite'
    def __unicode__(self):
        return self.titre  
# Create your models here.
