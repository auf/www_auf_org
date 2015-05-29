from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from auf.django.references.models import Region


class CarteCMSPlugin(CMSPluginBase):
    name = "Carte du monde"
    render_template = "cmsplugin_carte/base.html"
    admin_preview = False

    def render(self, context, instance, placeholder):
        context.update({'bureaux': Region.objects.filter(actif=1)})
        return context


plugin_pool.register_plugin(CarteCMSPlugin)
