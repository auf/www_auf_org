# encoding: utf-8
import os
from django.core.management.base import BaseCommand
from django.core.files import File as DjangoFile
from djangocms_text_ckeditor.models import Text
from cms.utils.copy_plugins import copy_plugins_to
from easy_thumbnails.exceptions import InvalidImageFormatError
from filer.models.imagemodels import Image
from djangocms_blog.models import BlogCategory, Post
from project.auf_site_institutionnel.models import Bourse, Actualite, Appel_Offre, Evenement, Publication  # , Veille


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
        p.save()

        # image
        if a.image and os.path.isfile(a.image.path):
            obj = Image(file=DjangoFile(open(a.image.path, 'rb')), name=a.image.name)
            obj.save()
            p.main_image = obj
            p.save()

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

        if args[0] == "clean" or args[0] == "test":
            print "cleaning"
            self._clean()
            if args[1] == "only":
                quit()

        for i in [Actualite, Bourse, Appel_Offre, Evenement, Publication]:
            counter = 0

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
                counter += 1
                if args[0] == "test" and counter >= 30:
                    break
