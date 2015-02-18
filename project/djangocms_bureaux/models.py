from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class Region(models.Model):
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255, db_index=True)

class BureauExtension(PageExtension):
    bureau = models.ManyToManyField(Region)
    
extension_pool.register(BureauExtension)
