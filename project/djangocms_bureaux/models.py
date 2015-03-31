from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from filer.fields.image import FilerImageField
from filer.models.filemodels import File
from filer.settings import FILER_ADMIN_ICON_SIZES

ICONES = {
    "pdf": "fa-file-pdf-o",
    "doc": "fa-file-word-o",
    "odt": "fa-file-text",
    "jpeg": "fa-file-image-o",
    "png": "fa-file-image-o",
    "jpg": "fa-file-image-o",
    "gif": "fa-file-image-o",
    "mp3": "fa-file-audio-o",
    "wav": "fa-file-audio-o",
    "mp4": "fa-file-video-o",
    "mov": "fa-file-video-o",
    "avi": "fa-file-video-o",
    "zip": "fa-file-archive-o"
}

#TAILLES = {
#    "16":"",
#    "32":"fa-2x",
#    "48":"fa-3x",
#    "64":"fa-4x",
#}


class AufFile(File):
    @property
    def icons(self):
        r = {}
        for size in FILER_ADMIN_ICON_SIZES:
            ext = self.extension
            if ext in ICONES.keys():
                r[size] = "/static/fonts/pngs/%s/.png" % (ICONES[ext])
            else:
                r[size] = "/static/fonts/pngs/fa-file-o.png"
        return r

    class Meta:
        proxy = True


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



