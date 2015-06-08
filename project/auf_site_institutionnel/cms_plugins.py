from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from auf.django.references.models import Etablissement, Pays, Implantation, Employe
from django.template import Context, RequestContext

from project.auf_site_institutionnel.filters import MembreFilter
from project.auf_site_institutionnel.filters import ImplantationFilter
from project.auf_site_institutionnel.models import Partenaire


#from newsletter.models import *
from .models import EmployePlugin, ImplantationPlugin


class CMSMembrePlugin(CMSPluginBase):
    name = _("Membre")
    render_template = "auf_site_institutionnel/membrePlugin.html"

    def render(self, context, instance, placeholder):
        dictFilter = {}
        dictFilter['membre'] = True
        # if request.method == 'GET': # If the form has been submitted...
        item_list = MembreFilter(
            context['request'].GET or None, queryset=Etablissement.objects.filter(**dictFilter))

        context.update({'membre_list': item_list,
                        'form': item_list.form,
                        'placeholder': placeholder})
        return context

plugin_pool.register_plugin(CMSMembrePlugin)


class CMSPartenairePlugin(CMSPluginBase):
    name = _("Partenaire")
    render_template = "auf_site_institutionnel/partenairePlugin.html"

    def render(self, context, instance, placeholder):
        item_list = Partenaire.objects.all()

        context.update({'partenaire_list': item_list,
                        'form': item_list,
                        'placeholder': placeholder})
        return context

plugin_pool.register_plugin(CMSPartenairePlugin)


class CMSEmployePlugin(CMSPluginBase):
    name = _("Employe")
    model = EmployePlugin
    render_template = "auf_site_institutionnel/employe/base.html"

    def render(self, context, instance, placeholder):
        ctx = super(CMSEmployePlugin, self).render(
            context, instance, placeholder)
        qs = Employe.objects.filter(actif=True)
        if instance.service:
            qs = qs.filter(service=instance.service)
        if instance.fonction:
            qs = qs.filter(fonction__contains=instance.fonction)
        if instance.region:
            qs = qs.filter(implantation__region=instance.region)

        ctx['object_list'] = qs
        ctx['layout_template'] = instance.layout_template
        return ctx

plugin_pool.register_plugin(CMSEmployePlugin)


class CMSImplantationPlugin(CMSPluginBase):
    name = _("Implantation")
    model = ImplantationPlugin
    render_template = "auf_site_institutionnel/_implantation.html"

    def render(self, context, instance, placeholder):
        ctx = super(CMSImplantationPlugin, self).render(
            context, instance, placeholder)
        qs = Implantation.objects.filter(actif=True)
        if instance.region:
            qs = qs.filter(region=instance.region)

        ctx['object_list'] = qs
        return ctx

plugin_pool.register_plugin(CMSImplantationPlugin)

# class CMSLettrePlugin(CMSPluginBase):
#    name = _("Lettre")
#    render_template = "auf_site_institutionnel/lettrePlugin.html"
#
#    def render(self, context, instance, slugRegion):
#        region_actuel = context['region_actuel']
#        print region_actuel
#        item_list = Newsletter.objects.filter(bureau__slug=region_actuel).filter(status='3').order_by('-date')[:20]
#
#        context.update({'lettre_list':item_list})
#        return context
#
# plugin_pool.register_plugin(CMSLettrePlugin)
#
#
# class CMSVideoPlugin(CMSPluginBase):
#    name = _("Video")
#    model = VideoPlugin
#    render_template = "auf_site_institutionnel/videoPlugin.html"
#
#    def render(self, context, instance, placeholder):
#        context.update({'videoG':instance.video,
#                        'video':instance,
#                        'placeholder':placeholder})
#        return context
#
# plugin_pool.register_plugin(CMSVideoPlugin)
