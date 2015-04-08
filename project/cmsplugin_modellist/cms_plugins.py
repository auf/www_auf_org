from django.db.models import get_model

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import ModelList, TEMPLATE_PATH, MODEL_LIST


class ModelListCMSPlugin(CMSPluginBase):
    model = ModelList
    name = "Liste des sous pages d'une section"
    render_template = "cmsplugin_modellist/base.html"
    admin_preview = False

    def render(self, context, instance, placeholder):
        ctx = super(ModelListCMSPlugin, self).render(context, instance, placeholder)

        obj = get_model('auf_site_institutionnel', instance.modele)
        bureau = instance.bureau.all()

        if bureau:
            ctx['object_list'] = obj.objects.filter(bureau=bureau)[:instance.nbelements]
        else:
            ctx['object_list'] = obj.objects.all()[:instance.nbelements]
        ctx['title'] = instance.title
        ctx['layout_template'] = instance.layout_template
        ctx['voir_plus'] = "/recherche/?selected_facets=section__" + MODEL_LIST[instance.modele]

        return ctx

plugin_pool.register_plugin(ModelListCMSPlugin)
