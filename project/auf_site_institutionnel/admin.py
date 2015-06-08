# coding: utf8
from project.auf_site_institutionnel.models import *
from django.db import models
from django.forms import ModelForm
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdminMixin, FrontendEditableAdminMixin


class RubriqueBureauAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ['titre']}
    fieldsets = [
        ('Cibles', {'fields': ['bureau']}),
        ('Article', {'fields': ['status','titre', 'slug', 'image', 'resume'], 'classes': ['wide']}),
                                # 'texte'], 'classes': ['wide']}),
    ]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "bureau":
            qs = Region.objects.all()
            if not request.user.is_superuser:
                qs = qs.exclude(id=999)
            kwargs["queryset"] = qs
        return super(RubriqueBureauAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def afficher_les_bureaux(self, obj):
        return ', '.join([b.nom for b in obj.bureau.filter(actif=1)])

    def show_image2(self, obj):
        if obj.image:
            return "<img src='../../../media/%s' style='height:40px;'>" % obj.image
        else:
            return "<img src='../../../static/logodefaut.jpg' style='height:40px;'>"
    show_image2.allow_tags = True #permet de sortir du html#
    show_image2.short_description = 'Image'

    list_display = ('status', 'show_image2', 'titre', 'date_pub', 'afficher_les_bureaux')
    list_display_links = ('status', 'titre')
    search_fields = ['titre']


class RubriqueBureauPersonnaAdmin(RubriqueBureauAdmin):
    def show_image2(self, obj):
        if obj.image:
            return "<img src='../../../media/%s' style='height:40px;'>" % obj.image
        else:
            return "<img src='../../../static/logodefaut.jpg' style='height:40px;'>"
    show_image2.allow_tags = True #permet de sortir du html#
    show_image2.short_description = 'Image'

    list_display = ('status', 'show_image2', 'titre', 'date_pub', 'afficher_les_bureaux', 'date_fin')
    fieldsets = [('Cibles', {'fields': ['bureau', 'personna']})] + \
	RubriqueBureauAdmin.fieldsets[1:]

    def afficher_les_personnas(self, obj):
        return ', '.join([b.nom for b in obj.personna.all()])

class PersonnaAdmin(admin.ModelAdmin):
    pass

class BourseAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin, RubriqueBureauPersonnaAdmin):

    fieldsets = RubriqueBureauPersonnaAdmin.fieldsets + [('Date', {'fields': ['date_fin', 'date_fin2'], 'classes': ['wide']}),]
    def queryset(self, request):
        """
        Filtrage de la liste par région.
        Attention : Étant donnée que le modèle Région ne fait pas partie du référentiel,
        on part du postulat que le id de la région est le même que dans le référentiel.
        """
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs


class Appel_OffreAdmin(PlaceholderAdminMixin, FrontendEditableAdminMixin, RubriqueBureauPersonnaAdmin):

    prepopulated_fields = {'slug': ['titre']}
    fieldsets = [
	('Partenaires?', {'fields': ['auf']}),
        ('Cibles', {'fields': ['bureau']}),
        ('Article', {'fields': ['status', 'titre', 'slug', 'image', 'resume'], 'classes': ['wide']}),
	('Date', {'fields': ['date_fin', 'date_fin2'], 'classes': ['wide']}),
    ]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "bureau":
            qs = Region.objects.all()
            if not request.user.is_superuser:
                qs = qs.exclude(id=999)
            kwargs["queryset"] = qs
        return super(RubriqueBureauAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def afficher_les_bureaux(self, obj):
        return ', '.join([b.nom for b in obj.bureau.filter(actif=1)])

    def show_image2(self, obj):
        if obj.image:
            return "<img src='../../../media/%s' style='height:40px;'>" % obj.image
        else:
            return "<img src='../../../static/logodefaut.jpg' style='height:40px;'>"
    show_image2.allow_tags = True #permet de sortir du html#
    show_image2.short_description = 'Image'

    list_display = ('status', 'show_image2', 'titre', 'date_pub', 'afficher_les_bureaux', 'auf')
    list_display_links = ('status', 'titre')
    search_fields = ['titre']

    def queryset(self, request):
        """
        Filtrage de la liste par région.
        Attention : Étant donnée que le modèle Région ne fait pas partie du référentiel,
        on part du postulat que le id de la région est le même que dans le référentiel.
        """
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs


class EvenementAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin, RubriqueBureauAdmin):
    def show_image2(self, obj):
        if obj.image:
            return "<img src='../../../media/%s' style='height:40px;'>" % obj.image
        else:
            return "<img src='../../../static/logodefaut.jpg' style='height:40px;'>"
    show_image2.allow_tags = True #permet de sortir du html#
    show_image2.short_description = 'Image'

    list_display = ('status', 'show_image2', 'titre', 'date_pub', 'afficher_les_bureaux', 'date_debut', 'date_fin')
    fieldsets = RubriqueBureauAdmin.fieldsets + [('Date', {'fields': ['date_debut', 'date_fin'], 'classes': ['wide']}),('Informations Supplémentaires', {'fields': ['lieu', 'detail_horaire'], 'classes': ['wide']})]
    def queryset(self, request):
        """
        Filtrage de la liste par région.
        Attention : Étant donnée que le modèle Région ne fait pas partie du référentiel,
        on part du postulat que le id de la région est le même que dans le référentiel.
        """
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs


class PublicationAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin):
    prepopulated_fields = {'slug': ['titre']}
    fieldsets = [
        ('Cibles', {'fields': ['bureau']}),
        ('Article', {'fields': ['status', 'titre', 'slug', 'image', 'docu', 'resume'], 'classes': ['wide']}),
        ('Date', {'fields': ['date_pub'], 'classes': ['wide']}),
    ]

    def afficher_les_bureaux(self, obj):
        return ', '.join([b.nom for b in obj.bureau.all()])

    def show_image2(self, obj):
        if obj.image:
            return "<img src='../../../media/%s' style='height:40px;'>" % obj.image
        else:
            return "<img src='../../../static/logodefaut.jpg' style='height:40px;'>"
    show_image2.allow_tags = True #permet de sortir du html#
    show_image2.short_description = 'Image'

    list_display = ('status', 'show_image2', 'titre', 'date_pub', 'afficher_les_bureaux')
    def queryset(self, request):
        """
        Filtrage de la liste par région.
        Attention : Étant donnée que le modèle Région ne fait pas partie du référentiel,
        on part du postulat que le id de la région est le même que dans le référentiel.
        """
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs

class ComaresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['titre']}
    fieldsets = [
        ('Cibles', {'fields': ['bureau']}),
        ('Article', {'fields': ['status', 'titre', 'slug', 'image', 'resume'], 'classes': ['wide']}),
        ('Date', {'fields': ['date_pub'], 'classes': ['wide']}),
    ]

    def afficher_les_bureaux(self, obj):
        return ', '.join([b.nom for b in obj.bureau.all()])

    def show_image2(self, obj):
        if obj.image:
            return "<img src='../../../media/%s' style='height:40px;'>" % obj.image
        else:
            return "<img src='../../../static/logodefaut.jpg' style='height:40px;'>"
    show_image2.allow_tags = True #permet de sortir du html#
    show_image2.short_description = 'Image'

    list_display = ('status', 'show_image2', 'titre', 'date_pub', 'afficher_les_bureaux')
    def queryset(self, request):

        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs


class ActualiteAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin, RubriqueBureauAdmin):
    frontend_editable_fields = ['titre', 'resume', "image"]
    fieldsets = RubriqueBureauAdmin.fieldsets + [('Date', {'fields': ['date_pub'], 'classes': ['wide']}),]
    list_display = ('status', 'show_image2', 'titre', 'date_pub', 'afficher_les_bureaux')
    def queryset(self, request):
        """
        Filtrage de la liste par région.
        Attention : Étant donnée que le modèle Région ne fait pas partie du référentiel,
        on part du postulat que le id de la région est le même que dans le référentiel.
        """
        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs


class VeilleAdmin(RubriqueBureauAdmin):
    fieldsets = RubriqueBureauAdmin.fieldsets + [('Date', {'fields': ['date_pub'], 'classes': ['wide']}),]
    def queryset(self, request):

        qs = self.model._default_manager.get_query_set()

        if request.user.is_superuser:
            return qs

        if request.user.employe is not None:
            return qs.filter(bureau=request.user.employe.implantation.region.id)

        return qs



#admin.site.register(Bureau, BureauAdmin)
admin.site.register(Veille, VeilleAdmin)
admin.site.register(Personna, PersonnaAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Actualite, ActualiteAdmin)
admin.site.register(Evenement, EvenementAdmin)
admin.site.register(Bourse, BourseAdmin)
admin.site.register(Appel_Offre, Appel_OffreAdmin)
admin.site.register(Comares, ComaresAdmin)
admin.site.register(Partenaire)
