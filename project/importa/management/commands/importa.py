# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File as DjangoFile

from cms import api
from cms.models import Page

from adminfiles.models import FileUpload
from adminfiles.parse import UPLOAD_RE

from filer.models.imagemodels import Image
#from filer.models.filemodels import File
from project.djangocms_bureaux.models import AufFile as File
from filer.models.foldermodels import Folder

from cmsplugin_filer_file.models import FilerFile
from cmsplugin_filer_file.cms_plugins import FilerFilePlugin


from project.auf_site_institutionnel.models import Actualite,\
    Bourse, Actualite, Veille, Appel_Offre, Evenement, Publication

#from project.djangocms_bureaux.models import ImageExtension


def _adminfile_to_filer(slug, ph, parent):
    try:
        upload = FileUpload.objects.get(slug=slug)
        print(upload.upload.file)
    except FileUpload.DoesNotExist:
        upload = None
        return ""

    # FIXME
    # if upload.is_image():
    folder = Folder.objects.all()[0]
    obj = File(
        file=DjangoFile(open(upload.upload.path, 'rb')), name=upload.upload.name)
    obj.folder = folder
    #obj._committed = False
    obj.save()
    #obj = File(open(upload.upload.path, 'rb'), name=upload.upload.name)
    #image = Image.objects.create(file=obj, original_filename=upload.upload.name)

    filer_file = api.add_plugin(
        ph, "FilerFilePlugin", "fr", target=parent, file=obj, title=upload.title)
    #filer_file = FilerFile(parent=parent, plugin_type="FilerFilePlugin", language="fr", title=upload.title, file=obj)
    # filer_file.save()
    return """<img src="/static/filer/icons/file_32x32.png" alt="%s" title="%s" id="plugin_obj_%s">""" % (upload.title, upload.title, filer_file.id)


class Command(BaseCommand):

    def handle(self, *args, **options):
        #page_actualite = api.create_page(u"Actualité", "trois_colonnes.html", "fr")
        # for i in [Bourse, Actualite, Veille, Appel_Offre, Evenement,
        # Publication]:
        for i in [Actualite, Bourse, Actualite, Veille, Appel_Offre, Evenement, Publication]:
            for a in i.objects.all():
                print(a.pk)
                # page = api.create_page(a.titre, "trois_colonnes.html", "fr", slug=a.slug,
                #                       meta_description=a.resume, publication_date=a.date_pub,
                #                       published=True, parent=page_actualite)
                # if a.image:
                #    obj = File(open(a.image.path, 'rb'), name=a.image.name)
                #    image = Image.objects.create(file=obj, original_filename=a.image.name)
                #    ImageExtension.objects.create(extended_object=page, image=image)

                #ph = page.placeholders.get(slot="texte")

                if a.cmstexte:
                    a.cmstexte.cmsplugin_set.all().delete()
                else:
                    a.save()
                texte = a.texte
                txt = api.add_plugin(a.cmstexte, "TextPlugin", "fr")
                for match in UPLOAD_RE.finditer(texte):
                    img = _adminfile_to_filer(match.group(1), a.cmstexte, txt)
                    texte = UPLOAD_RE.sub(img, texte)
                txt.body = texte
                txt.save()
