# encoding: utf-8
import sys

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File as DjangoFile

from cms import api
from cms.models import Page
from cms.utils.copy_plugins import copy_plugins_to

from adminfiles.models import FileUpload
from adminfiles.parse import UPLOAD_RE

from filer.models.imagemodels import Image
#from filer.models.filemodels import File
from project.djangocms_bureaux.models import AufFile as File
from filer.models.foldermodels import Folder

from cmsplugin_filer_file.models import FilerFile
from cmsplugin_filer_file.cms_plugins import FilerFilePlugin



from djangocms_blog.models import BlogCategory, Post

from project.auf_site_institutionnel.models import Actualite,\
    Bourse, Actualite, Veille, Appel_Offre, Evenement, Publication


class Command(BaseCommand):
    def handle(self, *args, **options):
        #page_actualite = api.create_page(u"Actualité", "trois_colonnes.html", "fr")
        #for i in [Bourse, Actualite, Veille, Appel_Offre, Evenement, Publication]:
        for i in [Actualite]: #, Bourse, Veille, Appel_Offre, Evenement, Publication]:
            for a in i.objects.all():
                print(a.pk)
                p = Post.objects.language('fr').create(
                        slug=a.slug,
                        publish=True,
                        title=a.titre,
                        date_published=a.date_pub,
                        date_modified=a.date_mod,
                        date_created=a.date_pub,
                        abstract=a.resume)
                # category
                p.categories.add(BlogCategory.objects.language('fr').get(id=107)) #slug=a._meta.model_name).blog_posts.add(p)
                # image
                if a.image:
                        obj = Image(file=DjangoFile(open(a.image.path, 'rb')), name=a.image.name)
                        obj.save()
                        p.main_image = obj
                        folder = Folder.objects.get(id=6)
                        obj.folder = folder
                        obj.save()
                # tags
                bureaux = a.bureau.all()
                if not bureaux or a.status == 3 or a.status == 5: p.tags.add("International")
                for bureau in bureaux:
                        p.tags.add(bureau.nom)

                # plugins
                copy_plugins_to(a.cmstexte.get_plugins(), p.content)
                p.save()

