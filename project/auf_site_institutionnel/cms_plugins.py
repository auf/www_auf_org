from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from auf.django.references.models import Etablissement, Pays, Implantation, Employe
from django.template import Context, RequestContext

from project.auf_site_institutionnel.filters import MembreFilter
from project.auf_site_institutionnel.filters import ImplantationFilter
from project.auf_site_institutionnel.models import Partenaire

#from newsletter.models import *
from .models import EmployePlugin

class CMSMembrePlugin(CMSPluginBase):
    name = _("Membre")
    render_template = "auf_site_institutionnel/membrePlugin.html"

    def render(self, context, instance, placeholder):
        dictFilter = {}
        dictFilter['membre'] = True
        #if request.method == 'GET': # If the form has been submitted...
        item_list = MembreFilter(context['request'].GET or None, queryset = Etablissement.objects.filter(**dictFilter))

        context.update({'membre_list':item_list,
                        'form':item_list.form,
                        'placeholder':placeholder})
        return context

plugin_pool.register_plugin(CMSMembrePlugin)


class CMSImplantationPlugin(CMSPluginBase):
    name = _("Implantation")
    render_template = "auf_site_institutionnel/implantationPlugin.html"

    def render(self, context, instance, placeholder):
        dictFilter = {}
        #dictFilter['implantation'] = True
        #if request.method == 'GET':
        item_list = ImplantationFilter(context['request'].GET or None, queryset = Implantation.ouvertes.filter(**dictFilter))

        context.update({'implantation_list':item_list,
                        'form':item_list.form,
                        'placeholder':placeholder})
        return context

plugin_pool.register_plugin(CMSImplantationPlugin)


class CMSPartenairePlugin(CMSPluginBase):
    name = _("Partenaire")
    render_template = "auf_site_institutionnel/partenairePlugin.html"

    def render(self, context, instance, placeholder):
        item_list = Partenaire.objects.all()

        context.update({'partenaire_list':item_list,
                        'form':item_list,
                        'placeholder':placeholder})
        return context

plugin_pool.register_plugin(CMSPartenairePlugin)


class CMSEmployePlugin(CMSPluginBase):
    name = _("Employe")
    model = EmployePlugin
    render_template = "auf_site_institutionnel/employePlugin.html"

    def render(self, context, instance, placeholder):
        ctx = super(CMSEmployePlugin, self).render(context, instance, placeholder)
        if instance.service:
            item_list = Employe.objects.filter(actif=True, service=instance.service)
        elif instance.fonction:
            item_list = Employe.objects.filter(actif=True, fonction=instance.fonction)
        elif instance.region:
            item_list = Employe.objects.filter(actif=True, implantation__region=instance.region)

        ctx['object_list'] = item_list
        return ctx

plugin_pool.register_plugin(CMSEmployePlugin)


#class CMSLettrePlugin(CMSPluginBase):
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
#plugin_pool.register_plugin(CMSLettrePlugin)
#
#
#class CMSVideoPlugin(CMSPluginBase):
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
#plugin_pool.register_plugin(CMSVideoPlugin)
