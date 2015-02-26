# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError

from cms import api
from cms.models import Page

from adminfiles.models import FileUpload
from adminfiles.parse import UPLOAD_RE

from project.importa.models import Actualite


def _adminfile_to_filer(slug, ph):
    try:
        upload = FileUpload.objects.get(slug=slug)
    except FileUpload.DoesNotExist:
        upload = None
        return ""

    # FIXME
    # if upload.is_image():
    #filer_file = api.add_plugin(ph, "FilerFilePlugin", "fr", file=upload.upload)
    #return """<img src="/static/filer/icons/file_32x32.png" alt="%s" title="%s" id="plugin_obj_%s">""" % (upload.title, upload.title, filer_file.id)
    return ""
    
class Command(BaseCommand):

    def handle(self, *args, **options):
        page_actualite = api.create_page(u"Actualité", "trois_colonnes.html", "fr")
        for a in Actualite.objects.all():
            print(a.pk)
            page = api.create_page(a.titre, "trois_colonnes.html", "fr", slug=a.slug,
                                   meta_description=a.resume, publication_date=a.date_pub,
                                   published=True, parent=page_actualite)
            ph = page.placeholders.get(slot="texte")

            texte = a.texte
            for match in UPLOAD_RE.finditer(texte):
                img = _adminfile_to_filer(match.group(1), ph)
                texte = UPLOAD_RE.sub(img, texte)
            api.add_plugin(ph, "TextPlugin", "fr", body=texte)
