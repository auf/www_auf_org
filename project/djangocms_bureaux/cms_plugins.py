from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin


class NbInstitutionsPlugin(CMSPluginBase):
    name = "Nb institutions"
    module = "auf"
    text_enabled = True
    model = CMSPlugin
    render_template = "NB.html"

    def render(self, context, instance, placeholder):
        context = super(NbInstitutionsPlugin, self).render(
            context, instance, placeholder)
        context['object'] = 804

        return context

plugin_pool.register_plugin(NbInstitutionsPlugin)
