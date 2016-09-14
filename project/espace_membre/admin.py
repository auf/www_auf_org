# -*- encoding: utf-8 -*-
from datetime import date

from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput

import project.espace_membre.models as espace_membre
from django.forms.models import BaseInlineFormSet


class ResponsableFormSet(BaseInlineFormSet):

    def save(self, commit=True):
        objects = super(ResponsableFormSet, self).save(commit)
        for object in objects:
            if object.type != self.type_responsable:
                object.type = self.type_responsable
                if commit:
                    object.save()
        return objects


class ResponsableInline(admin.StackedInline):
    template = 'admin/espace_membre/edit_inline.html'
    model = espace_membre.ResponsableModification
    extra = 0
    fields = ('salutation', 'nom', 'prenom',
              'courriel', 'fonction', 'sousfonction', )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80'})}, }

    formset = ResponsableFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(ResponsableInline, self).get_formset(
            request, obj, **kwargs)
        formset.type_responsable = self.type_responsable
        return formset


class ResponsablePHAInline(ResponsableInline):
    verbose_name = u'Responsable PHA'
    verbose_name_plural = u'Responsables PHA'
    type_responsable = espace_membre.RESPONSABLE_ETABLISSEMENT

    def get_type_responsable(self):
        return

    def queryset(self, request):
        queryset = super(ResponsablePHAInline, self).queryset(request)
        queryset = queryset.filter(
            type=espace_membre.RESPONSABLE_ETABLISSEMENT)
        return queryset


class ResponsableComInline(ResponsableInline):
    verbose_name = u'Responsable Com'
    verbose_name_plural = u'Responsables Com'
    type_responsable = espace_membre.RESPONSABLE_COMMUNICATION

    def queryset(self, request):
        queryset = super(ResponsableComInline, self).queryset(request)
        queryset = queryset.filter(
            type=espace_membre.RESPONSABLE_COMMUNICATION)
        return queryset


class CourrielAdmin(admin.ModelAdmin):
    fields = ('sujet', 'contenu')
    list_display = ('id', 'sujet', 'date_creation')

    def save_model(self, request, obj, form, change):
        obj.user_creation = request.user
        obj.save()


admin.site.register(
    espace_membre.Courriel, CourrielAdmin
)


class AccesAdmin(admin.ModelAdmin):
    search_fields = ('etablissement__nom',)

    def queryset(self, request):
        qs = super(AccesAdmin, self).queryset(request)
        return qs.filter(active=True)

admin.site.register(
    espace_membre.Acces, AccesAdmin
)


class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sigle', 'date_validation_etablissement',
                    'validation_etablissement', 'date_validation_sai',
                    'validation_sai', 'date_validation_com', 'validation_com')
    list_filter = ('validation_etablissement',)
    inlines = (ResponsablePHAInline, ResponsableComInline, )
    search_fields = ('nom', 'sigle')
    actions = ('faire_valider_par_sai',)
    fieldsets = (
        (u"Renseignements généraux", {
            'fields': (
                'nom',
                'sigle',
            )
        }
        ),
        (u"Contacts", {
            'fields': (
                'pays', 'adresse', 'code_postal', 'ville', 'cedex',
                'province', 'telephone', 'fax', 'courriel', 'url',
            )
        }
        ),
        (u"Statistiques", {
            "fields": ('nombre',)
        }
        ),
        (u"Informations Annuaire", {
            "fields": ('historique', 'description', 'chiffres_cles')
        }
        ),
        (u"Validation", {
            'fields': (
                ('validation_sai', 'date_validation_sai',),
                ('validation_com', 'date_validation_com',),
                ('validation_etablissement',
                 'date_validation_etablissement'),
                ('export_gde_sai', 'export_gde_com'),
            )
        }
        ),
    )
    readonly_fields = (
        'date_validation_sai', 'date_validation_etablissement', 'date_validation_com')

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80'})}, }

    def faire_valider_par_sai(self, request, queryset):
        queryset.update(validation_sai=True, date_validation_sai=date.today())

    faire_valider_par_sai.short_description = u"Valider par SAI"

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.modification_par = request.user.username
            instance.save()
        formset.save_m2m()

    def queryset(self, request):
        queryset = super(EtablissementAdmin, self).queryset(request)
        queryset.select_related('etablissement')
        return queryset

    def change_view(self, request, object_id, form_url='', extra_context=None):
        response = super(EtablissementAdmin, self).change_view(
            request, object_id, form_url, extra_context)
        if request.POST.get('_save') == u'Valider et retourner à la liste':
            espace_membre.EtablissementModification.objects\
                .filter(id=object_id)\
                .update(validation_sai=True, date_validation_sai=date.today())
        return response

admin.site.register(
    espace_membre.EtablissementModification, EtablissementAdmin
)
