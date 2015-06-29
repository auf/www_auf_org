# encoding: utf-8

from django.db.models import get_model

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ModelList

FACETS = {
    'Actualite': 'Actualité',
    'Publication': 'Publication',
    'Appel_Offre': 'Appel d\'offre',
    'Bourse': 'Bourse',
    'Evenement': 'Événements',
    'Partenaire': 'Partenaires',
    'Comares': 'Comares',
    'Veille': 'Veilles',
}

SLUGS_REGION = {
    'Actualite': 'actualites',
    'Publication': 'publications',
    'Appel_Offre': 'appels-offre',
    'Evenement': 'evenements',
    'Veille': 'veille',
    'Bourse': 'allocations',
}


class ModelListCMSPlugin(CMSPluginBase):
    model = ModelList
    name = "Liste des sous pages d'une section"
    render_template = "cmsplugin_modellist/base.html"
    admin_preview = False

    def render(self, context, instance, placeholder):
        ctx = super(ModelListCMSPlugin, self).render(
            context, instance, placeholder)

        obj = get_model('auf_site_institutionnel', instance.modele)
        obj_query = obj.objects.exclude(status__in=[1, 2, 4]).order_by('-date_pub')
        bureau = instance.bureau.all()

        if bureau:
            ctx['object_list'] = obj_query.filter(
                bureau=bureau, status__in=[3,6]).distinct()[:instance.nbelements]
        else:
            ctx['object_list'] = obj_query.filter(status__in=[3,5]).distinct()[:instance.nbelements]
        ctx['title'] = instance.title

        # FIXME
        try:
            ctx['slug_region'] = SLUGS_REGION[instance.modele]
        except:
            pass

        ctx['layout_template'] = instance.layout_template

        # FIXME Flux RSS par bureau
        ctx['voir_plus'] = "/recherche/?selected_facets=section__" + \
            FACETS[instance.modele]
        ctx['lien_rss'] = "/flux/" + \
            instance.modele.lower() + "/?region_actuel=International"

        return ctx

plugin_pool.register_plugin(ModelListCMSPlugin)
