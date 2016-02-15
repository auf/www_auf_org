from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import MailmanPluginModel


class MailmanPlugin(CMSPluginBase):
    model = MailmanPluginModel
    render_template = "cmsplugin_mailman/plugin.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(MailmanPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(MailmanPlugin)
