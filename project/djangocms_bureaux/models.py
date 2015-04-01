from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from filer.fields.image import FilerImageField
from filer.models.filemodels import File
from filer.settings import FILER_ADMIN_ICON_SIZES

ICONES = {
    "pdf": "file-pdf-o",
    "doc": "file-word-o",
    "odt": "file-text",
    "jpeg": "file-image-o",
    "png": "file-image-o",
    "jpg": "file-image-o",
    "gif": "file-image-o",
    "mp3": "file-audio-o",
    "wav": "file-audio-o",
    "mp4": "file-video-o",
    "mov": "file-video-o",
    "avi": "file-video-o",
    "zip": "file-archive-o"
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
                r[size] = "/static/fonts/pngs/%s.png" % (ICONES[ext])
            else:
                r[size] = "/static/fonts/pngs/file-o.png"
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



