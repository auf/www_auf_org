from django.db import models


class OffreEmploi(models.Model):
    titre_poste = models.CharField(max_length=200, blank=True, null=True)
    metier = models.CharField(max_length=50, blank=True, null=True)
    type_contrat = models.CharField(max_length=45, blank=True, null=True)
    lieu = models.CharField(max_length=45, blank=True, null=True)
