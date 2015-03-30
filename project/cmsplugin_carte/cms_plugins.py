from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


class CarteCMSPlugin(CMSPluginBase):
    name = "Carte du monde"
    render_template = "cmsplugin_carte/base.html"
    admin_preview = False

plugin_pool.register_plugin(CarteCMSPlugin)
