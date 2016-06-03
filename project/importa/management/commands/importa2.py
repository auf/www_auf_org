# encoding: utf-8
import sys
import os
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File as DjangoFile
from django.db import transaction
from djangocms_text_ckeditor.models import Text
from cms import api
from cms.models import Page
from cms.utils.copy_plugins import copy_plugins_to
from adminfiles.models import FileUpload
from adminfiles.parse import UPLOAD_RE
from easy_thumbnails.exceptions import InvalidImageFormatError
from filer.models.imagemodels import Image
#from filer.models.filemodels import File
from project.djangocms_bureaux.models import AufFile as File
from filer.models.foldermodels import Folder
from cmsplugin_filer_file.models import FilerFile
from cmsplugin_filer_file.cms_plugins import FilerFilePlugin


from djangocms_blog.models import BlogCategory, Post

from project.auf_site_institutionnel.models import Bourse, Actualite, Veille, Appel_Offre, Evenement, Publication


class Command(BaseCommand):

    category_ids = {}

    def __init__(self):
        super(Command, self).__init__()

        categories = BlogCategory.objects.language('fr').all()

        for category in categories:
            if category.slug == 'actualites':
                self.category_ids['Actualite'] = category.id
            elif category.slug == 'allocations':
                self.category_ids['Bourse'] = category.id
            elif category.slug == 'appels-offre':
                self.category_ids['Appel_Offre'] = category.id
            elif category.slug == 'evenements':
                self.category_ids['Evenement'] = category.id
            elif category.slug == 'publications':
                self.category_ids['Publication'] = category.id

    def _clean(self):
        Post.objects.language('fr').filter(categories__in=[
            self.category_ids['Actualite'],
            self.category_ids['Bourse'],
            self.category_ids['Appel_Offre'],
            self.category_ids['Evenement'],
            self.category_ids['Publication']
        ]).delete()

    def _create_post(self, a, i):
        p = Post.objects.language('fr').create(
            slug=a.slug,
            publish=True,
            title=a.titre,
            date_published=a.date_pub,
            date_modified=a.date_mod,
            date_created=a.date_pub,
            abstract=a.resume,
        )

        # category
        p.categories.add(BlogCategory.objects.language('fr').get(id=self.category_ids[i.__name__]))

        # image
        if a.image and os.path.isfile(a.image.path):
            # print a.image.path
            obj = Image(file=DjangoFile(open(a.image.path, 'rb')), name=a.image.name)
            obj.save()
            p.main_image = obj
            print p.main_image
            p.save()

            # folder = Folder.objects.get(id=6)
            # obj.folder = folder
            # obj.save()

        # tags
        bureaux = a.bureau.all()
        if not bureaux or a.status == 3 or a.status == 5:
            p.tags.add("International")
        for bureau in bureaux:
            p.tags.add(bureau.nom)

        # plugins
        for plugin in a.cmstexte.get_plugins():
            if plugin.plugin_type == "TextPlugin":
                text = Text.objects.get(cmsplugin_ptr_id=plugin.id)
                p.post_text = text.body
                p.save()

            else:
                try:
                    copy_plugins_to(a.cmstexte.get_plugins(), p.content, to_language="fr")
                except InvalidImageFormatError:
                    continue

    def handle(self, *args, **options):

        if len(args) == 1 and args[0] == "clean":
            print "cleaning"
            self._clean()

        for i in [Actualite, Bourse, Appel_Offre, Evenement, Publication]:

            for a in i.objects.all():
                print "Original: %s %d - %s" % (i.__name__, a.pk, a.slug)
                if not a.date_pub:
                    a.date_pub = a.date_mod
                while Post.objects.language('fr').filter(translations__slug=a.slug):
                    if len(a.slug) < 50:
                        a.slug += "2"
                    else:
                        a.slug = a.slug[:-1] + "2"

                self._create_post(a, i)

