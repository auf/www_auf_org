from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import (
  PageList,
  TEMPLATE_PATH,
)

class PageListCMSPlugin(CMSPluginBase):
    model = PageList
    name = "Liste des sous pages"
    render_template = "cmsplugin_pagelist/base.html"
    admin_preview = False

    def render(self, context, instance, placeholder):

        try:
            # If there's an exception (500), default context_processors may not be called.
            request = context['request']
        except KeyError:
            return "There is no  `request` object in the context."

        root_page = instance.root
        root_page_url = root_page.get_absolute_url()
        nbelements = instance.nbelements

        return context

plugin_pool.register_plugin(PageListCMSPlugin)
