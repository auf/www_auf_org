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
        ctx = super(PageListCMSPlugin, self).render(context, instance, placeholder)

        ctx['descendants'] = instance.root.get_descendants()[:instance.nbelements]
        ctx['title'] = instance.title

        return ctx

plugin_pool.register_plugin(PageListCMSPlugin)
