# encoding: utf-8
import os
import datetime
from django.conf import settings
from django.contrib.auth.models import AnonymousUser

from django.core.management.base import BaseCommand
from django.template import RequestContext
from django.test.client import RequestFactory
import djangocms_blog.models as blog_models
import filer.models as filer_models
from django.db import transaction
import shutil
import resource

from project.auf_site_institutionnel.models import (
     Bourse, Actualite, Veille, Appel_Offre, Evenement, Publication)


# http://stackoverflow.com/questions/26337120/django-cms-how-to-get-placeholder-html-content
def render_placeholder_html(placeholder):
    from cms import plugin_rendering
    request_factory = RequestFactory()
    request = request_factory.get('/')
    request.session = {}
    request.LANGUAGE_CODE = settings.LANGUAGE_CODE

    # Needed for plugin rendering.
    request.current_page = None
    request.user = AnonymousUser()
    return plugin_rendering.render_placeholder(placeholder,
                                               RequestContext(request))


class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self, *args, **options):
        testing = "test" in args
        sp = transaction.savepoint()
        try:
            actualites = blog_models.BlogCategory.objects.create(
                name=u"Actualités", slug="actualites")
            veilles = blog_models.BlogCategory.objects.create(name=u"Veilles",
                                                              slug="veille")
            appels_offres = blog_models.BlogCategory.objects.create(
                name=u"Appels d'offres", slug="appels_offres")
            evenements = blog_models.BlogCategory.objects.create(
                name=u"Évènements", slug="evenements")
            publications = blog_models.BlogCategory.objects.create(
                name=u"Publications", slug="publication")
            bourse = blog_models.BlogCategory.objects.create(name=u"Bourse",
                                                             slug="bourse")
            categories = {
                Actualite: actualites,
                Bourse: bourse,
                Veille: veilles,
                Appel_Offre: appels_offres,
                Evenement: evenements,
                Publication: publications
            }
            old_models = categories.keys()

            for i in old_models:
                for a in i.objects.all():
                    print(a.id)
                    if hasattr(a, 'date_debut'):
                        date_debut = a.date_debut
                    else:
                        date_debut = a.date_pub
                    try:
                        post = blog_models.Post.objects\
                            .translated(slug=a.slug)[0]
                    except IndexError:
                        # noinspection PyArgumentList
                        post = blog_models.Post(
                            date_created=date_debut,
                            date_modified=a.date_mod,
                            date_published=(a.date_pub or
                                            datetime.datetime.now()),
                            date_published_end=getattr(a, 'date_fin', None),
                            title=a.titre,
                            slug=a.slug,
                            abstract=a.resume,
                            post_text=render_placeholder_html(a.cmstexte)
                        )
                        if a.image:
                            if testing:
                                create_test_image(a.image)
                            image, _ = filer_models.Image.objects.get_or_create(
                                file=a.image.file, defaults={
                                    'name': a.slug, 'description': a.titre
                                })
                            post.main_image = image
                        tags = []
                        if a.status in ('5', '3'):
                            tags.append('International')
                        if a.status in ('6', '3'):
                            for region in a.bureau.all():
                                tags.append(u"B" + region.code)
                        post.save()
                        post.tags.set(*tags)
                        if a.image:
                            a.image.close()
                    post.categories.add(categories[a.__class__])
        finally:
            if testing:
                transaction.savepoint_rollback(sp)
            else:
                transaction.savepoint_commit(sp)


def create_test_image(image):
    image_filename = os.path.join(settings.MEDIA_ROOT,
                                  image.name)
    image_path = os.path.dirname(image_filename)
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    if not os.path.exists(image_filename):
        shutil.copy("/media/benselme/data/dev/projects/auf/"
                    "www_auf_org/sitestatic/img/logo.png",
                    image_filename)
