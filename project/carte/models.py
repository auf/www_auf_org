from django.db import models
import auf.django.references.models as auf_refs


class CoordonneesImplantations(models.Model):
    implantation = models.ForeignKey(auf_refs.Implantation)
    latitude = models.DecimalField(decimal_places=4, max_digits=8)
    longitude = models.DecimalField(decimal_places=4, max_digits=8)
    valide = models.BooleanField()
