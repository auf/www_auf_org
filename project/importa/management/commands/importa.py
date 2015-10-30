# encoding: utf-8
from django.conf import settings
from django.contrib.auth.models import AnonymousUser

from django.core.management.base import BaseCommand
from django.template import RequestContext
from django.test.client import RequestFactory
import djangocms_blog.models as blog_models
import filer.models as filer_models
from django.db import transaction

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
        sp = transaction.savepoint()
        try:
            actualites = blog_models.BlogCategory.objects.create(name=u"Actualités",
                                                                 slug="actualites")
            veilles = blog_models.BlogCategory.objects.create(name=u"Veilles",
                                                              slug="veille")
            appels_offres = blog_models.BlogCategory.objects.create(
                name=u"Appels d'offres", slug="appels_offres")
            evenements = blog_models.BlogCategory.objects.create(name=u"Évènements",
                                                                 slug="evenements")
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
                    # noinspection PyArgumentList
                    post = blog_models.Post(
                        date_created=a.date_debut,
                        date_modified=a.date_mod,
                        date_published=a.date_pub,
                        date_published_end=a.date_fin,
                        title=a.titre,
                        slug=a.slug,
                        abstract=a.resume,
                        post_text=render_placeholder_html(a.cmstexte)
                    )

                    image = filer_models.Image.objects.get_or_create(
                        file=a.image.file, defaults={
                            'name': a.slug, 'description': a.titre
                        })

                    post.main_image = image
                    post.categories.add()
                    tags = []
                    if a.status in ('5', '3'):
                        tags.append('International')
                    if a.status in ('6', '3'):
                        for region in a.bureau_set.all():
                            tags.append(region.nom)
                    post.save()
        finally:
            transaction.savepoint_rollback(sp)
