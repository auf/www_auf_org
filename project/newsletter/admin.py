# coding: utf8
import csv
from project.newsletter.models import *
from django.contrib import admin
from django import forms
from django.db import models
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect 
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.mail import send_mail

class NewsletterAdmin(admin.ModelAdmin):

    def queryset(self, request):
        
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs

    actions = ['envoyer_newsletter']
    
    class EnvoiForm(forms.Form):
        envoi = forms.CharField(widget=forms.MultipleHiddenInput) 
        
    def envoyer_newsletter(self, request, queryset):
    
        abonnes = Abonne.objects.all()
        form = None     
        
        if 'cancel' in request.POST:
            form = self.EnvoiForm(request.POST)
            self.message_user(request, 'BLAVLALALDADLA')
            return

        if not form:
            self.message_user(request, 'PAS DE FORM')
            
        return render_to_response('admin/send_mail.html', {'newsletter': queryset, 'form': form, 'abonnes_list': abonnes, 'path':request.get_full_path()}, context_instance = RequestContext(request))
        
    envoyer_newsletter.short_description = "Envoyer la lettre a votre liste de diffusion"
    
    fieldsets = [
        ('Informations', {'fields': ['status','numero','date','bureau']}),
        ('À la une', {'fields': ['titre_dossier','photo_dossier','texte_dossier','lien_dossier'], 'classes': ['wide']}),
        ('Bloc appels d\'offres', {'fields': ['appel'], 'classes': ['wide']}),
        ('Bloc actualités', {'fields': ['actualite', 'evenement', 'publication'], 'classes': ['wide']}),
        ('Liens utils', {'fields': ['lien', 'lien2', 'lienFace'], 'classes': ['collapse']}),
        ('Information du footer', {'fields': ['footer', 'abonne'], 'classes': ['collapse']}),
    ]
    
    def bureaux(self, obj):
        return ', '.join([b.nom for b in obj.bureau.all()])
        
    def show_nom(self, obj):
      return "<strong>Lettre d'information N %s</strong>" % obj.numero
    show_nom.allow_tags = True
    show_nom.short_description = 'Titre'
    
    def preview(self, obj):
      return "<a href='/lettre-information/%s' target='_blank'><img src='/static/img/html.png' height='16'> Visualiser</a>" % obj.id
    preview.allow_tags = True
    preview.short_description = 'Visualiser'
        
    list_display = ('show_nom','status','date','preview','bureaux')
    list_display_links = ('status', 'show_nom')
    search_fields = ['numero']
    
    def queryset(self, request):
        
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs
        
        
class FilAdmin(admin.ModelAdmin):

    def queryset(self, request):
        
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs
    
    fieldsets = [
        ('Informations', {'fields': ['numero', 'date','bureau']}),
        ('Contenu principal', {'fields': ['actualite', 'evenement'], 'classes': ['wide']}),
        ('Information du footer', {'fields': ['footer'], 'classes': ['collapse']}),
    ]
    
    def bureaux(self, obj):
        return ', '.join([b.nom for b in obj.bureau.all()])
        
    def show_nom(self, obj):
      return "<strong>Fil actualité N %s</strong>" % obj.numero
    show_nom.allow_tags = True
    show_nom.short_description = 'Titre'
    
    def preview(self, obj):
      return "<a href='/fil-actualites/%s' target='_blank'><img src='/static/img/html.png' height='16'> Visualiser</a>" % obj.id
    preview.allow_tags = True
    preview.short_description = 'Visualiser'
        
    list_display = ('show_nom','date','preview')
    list_display_links = ('show_nom',)
    search_fields = ['numero']


class BreveAdmin(admin.ModelAdmin):

    adminfiles_fields = ('texte_intro', 'texte_rh', 'texte_ari','texte_agenda', 'texte_mission', 'texte_arrive')
    
    fieldsets = [
        ('Informations', {'fields': ['numero', 'date']}),
        ('Texte introduction', {'fields': ['texte_intro'], 'classes': ['wide']}),
        ('Texte RH', {'fields': ['texte_rh'], 'classes': ['wide']}),
        ('Texte ARI', {'fields': ['texte_ari'], 'classes': ['wide']}),
        ('Texte agenda recteur', {'fields': ['texte_agenda'], 'classes': ['wide']}),
        ('Texte prochainement en mission', {'fields': ['texte_mission'], 'classes': ['wide']}),
        ('Texte arrivés-départs', {'fields': ['texte_arrive'], 'classes': ['wide']}),
        ('Texte divers', {'fields': ['texte_diver'], 'classes': ['wide']}),
        ('Texte autres infos', {'fields': ['texte_autre'], 'classes': ['wide']}),
        ('Texte pied de page', {'fields': ['footer'], 'classes': ['collapse']}),
    ]
        
    def show_nom(self, obj):
      return "<strong>Brèves N %s</strong>" % obj.numero
    show_nom.allow_tags = True
    show_nom.short_description = 'Titre'
    
    def preview(self, obj):
      return "<a href='/breves/%s' target='_blank'><img src='/static/img/html.png' height='16'> Visualiser</a>" % obj.id
    preview.allow_tags = True
    preview.short_description = 'Visualiser'
        
    list_display = ('show_nom','date','preview')
    list_display_links = ('show_nom',)
    search_fields = ['numero']
    
    
class ProjetPlaneteInline(admin.TabularInline):
    model = ProjetPlanete
    extra = 1
    
class MembrePlaneteInline(admin.TabularInline):
    model = MembrePlanete
    extra = 1
    
class PlaneteAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Informations', {'fields': ['status','numero', 'date']}),
        ('Dossier du mois', {'fields': ['titre_dossier', 'photo_dossier', 'texte_dossier', 'lien_dossier'], 'classes': ['wide']}),
        ('Agenda et appels d\'offres', {'fields': ['evenement_planete', 'appel_planete', 'bourse_planete'], 'classes': ['wide']}),
        ('En bref', {'fields': ['fil_planete'], 'classes': ['wide']}),
        ('Information du footer', {'fields': ['footer'], 'classes': ['collapse']}),
    ]
    
    inlines = [ProjetPlaneteInline, MembrePlaneteInline]
        
    def show_nom(self, obj):
      return "<strong>Planète AUF N %s</strong>" % obj.numero
    show_nom.allow_tags = True
    show_nom.short_description = 'Titre'
    
    def preview(self, obj):
      return "<a href='/planete-auf/%s' target='_blank'><img src='/static/img/html.png' height='16'> Visualiser</a>" % obj.id
    preview.allow_tags = True
    preview.short_description = 'Visualiser'
        
    list_display = ('show_nom','date','preview')
    list_display_links = ('show_nom',)
    search_fields = ['numero']
    

class AbonneAdmin(admin.ModelAdmin):
    
    def queryset(self, request):
        
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs
    
    actions = ['changestat','exporter']

    def changestat(self, request, queryset):
        valide = queryset.update(valide=1)
        if valide == 1:
            message_bit = "1 abonné a été validé"
        else:
            message_bit = "%s abonnés ont été validés" % valide
        self.message_user(request, "%s avec succès" % message_bit)
    changestat.short_description = "Valider le status"
    
    def exporter(self, request, queryset):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Abonnes_newsletter.csv"'

        writer = csv.writer(response)
        writer.writerow(['Adresse'])
        for b in queryset:
            writer.writerow([b.adresse])

        return response
    
    def bureaux(self, obj):
        return ', '.join([b.nom for b in obj.bureau.all()])
        
    def show_nom(self, obj):
      return "<strong>Lettre d'information N %s</strong>" % obj.numero
    show_nom.allow_tags = True
    show_nom.short_description = 'Titre'
    
    def preview(self, obj):
      return "<strong>Visualiser</strong>"
    preview.allow_tags = True
    preview.short_description = 'Visualiser'
        
    list_display = ('adresse','date','bureaux','valide')
    search_fields = ['adresse']
    

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Fil, FilAdmin)
admin.site.register(Breve, BreveAdmin)
admin.site.register(Planete, PlaneteAdmin)
admin.site.register(Abonne, AbonneAdmin)