# encoding: utf-8

from django.db.models import get_model

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import ModelList, TEMPLATE_PATH

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


class ModelListCMSPlugin(CMSPluginBase):
    model = ModelList
    name = "Liste des sous pages d'une section"
    render_template = "cmsplugin_modellist/base.html"
    admin_preview = False

    def render(self, context, instance, placeholder):
        ctx = super(ModelListCMSPlugin, self).render(context, instance, placeholder)

        obj = get_model('auf_site_institutionnel', instance.modele)
        obj_query = obj.objects.filter(status=3).order_by('-date_pub')
        bureau = instance.bureau.all()

        if bureau:
            ctx['object_list'] = obj_query.filter(bureau=bureau)[:instance.nbelements]
        else:
            ctx['object_list'] = obj_query[:instance.nbelements]
        ctx['title'] = instance.title
        ctx['layout_template'] = instance.layout_template

        # FIXME Flux RSS par bureau
        ctx['voir_plus'] = "/recherche/?selected_facets=section__" + FACETS[instance.modele]
        ctx['lien_rss'] = "/rss/" + instance.modele + "/?region_actuel=International"

        return ctx

plugin_pool.register_plugin(ModelListCMSPlugin)
