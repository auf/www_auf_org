# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.plugin_pool import plugin_pool
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_blog.cms_plugins import BlogPlugin
from djangocms_blog.models import BlogCategory
from project.djangocms_blog_singlepost_plugin.models import SingleEntry


class BlogSingleEntryPlugin(BlogPlugin):
    name = _('Single entry')
    model = SingleEntry

    def render(self, context, instance, placeholder):
        context = super(BlogSingleEntryPlugin, self).render(context, instance, placeholder)
        context['post'] = instance.get_posts(context['request'])  # , published_only=False)
        return context

plugin_pool.register_plugin(BlogSingleEntryPlugin)
