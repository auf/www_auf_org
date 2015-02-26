from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from filer.fields.image import FilerImageField

class Region(models.Model):
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255, db_index=True)

class BureauExtension(PageExtension):
    bureau = models.ManyToManyField(Region)
    
    
    def copy_relations(self, oldinstance, language):
        for bureau in oldinstance.bureau.all():
            self.bureau.add(bureau)

extension_pool.register(BureauExtension)


class ImageExtension(PageExtension):
    image = FilerImageField()
    
extension_pool.register(ImageExtension)



