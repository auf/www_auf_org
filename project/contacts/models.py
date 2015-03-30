from django.db import models

from auf.django.references.models import Region


class Contacte(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField()
    bureau = models.OneToOneField(Region)

    def __unicode__(self):
	return u'%s %s'%(self.nom, self.prenom)
