# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from djangocms_blog.cms_plugins import BlogLatestEntriesPlugin
from django.utils.translation import ugettext_lazy as _
from project.djangocms_bureaux.forms import AUFLatestEntriesForm
from project.djangocms_bureaux.models import LatestNews, LatestGrants, \
    LatestEvents, LatestPublications, LatestRequestsForProposal


class AUFPlugin(BlogLatestEntriesPlugin):
    module = "AUF"
    render_template = 'latest_entries.html'
    fields = ('latest_posts', 'tags')
    form = AUFLatestEntriesForm


class AUFLatestNewsPlugin(AUFPlugin):

    name = _("Latest News")
    model = LatestNews

    def render(self, context, instance, placeholder):
        context = super(AUFPlugin, self).render(
            context, instance, placeholder
        )
        context['category'] = "actualites"
        return context


class AUFLatestRequestsForProposalPlugin(AUFPlugin):

    name = _("Latest Requests for proposal")
    model = LatestRequestsForProposal

    def render(self, context, instance, placeholder):
        context = super(AUFPlugin, self).render(
            context, instance, placeholder
        )
        context['category'] = "appels-offre"
        return context


class AUFLatestGrantsPlugin(AUFPlugin):

    name = _("Latest Grants")
    model = LatestGrants

    def render(self, context, instance, placeholder):
        context = super(AUFPlugin, self).render(
            context, instance, placeholder
        )
        context['category'] = "allocations"
        return context


class AUFLatestEventsPlugin(AUFPlugin):

    name = _("Latest Events")
    model = LatestEvents

    def render(self, context, instance, placeholder):
        context = super(AUFPlugin, self).render(
            context, instance, placeholder
        )
        context['category'] = "evenements"
        return context


class AUFLatestPublicationsPlugin(AUFPlugin):

    name = _("Latest Publications")
    model = LatestPublications

    def render(self, context, instance, placeholder):
        context = super(AUFPlugin, self).render(
            context, instance, placeholder
        )
        context['category'] = "publications"
        return context


class NbInstitutionsPlugin(CMSPluginBase):
    name = "Nb institutions"
    module = "AUF"
    text_enabled = True
    model = CMSPlugin
    render_template = "NB.html"

    def render(self, context, instance, placeholder):
        context = super(NbInstitutionsPlugin, self).render(
            context, instance, placeholder)
        context['object'] = 804

        return context

plugin_pool.register_plugin(NbInstitutionsPlugin)
plugin_pool.register_plugin(AUFLatestNewsPlugin)
plugin_pool.register_plugin(AUFLatestRequestsForProposalPlugin)
plugin_pool.register_plugin(AUFLatestGrantsPlugin)
plugin_pool.register_plugin(AUFLatestEventsPlugin)
plugin_pool.register_plugin(AUFLatestPublicationsPlugin)
