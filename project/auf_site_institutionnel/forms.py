# -*- encoding: utf-8 -*-
import re
import datetime
from django import forms
from django import db
from django.db.models import Q
from django.db import models
from django.contrib.admin import widgets
from django.utils.safestring import mark_safe
#from captcha.fields import CaptchaField
from auf.django.references.models import Etablissement, Pays, Implantation, Service, Employe, Region
from django.conf import settings
from project.auf_site_institutionnel.models import Bourse, Personna, Actualite


class ContactEmployeForm(forms.Form):
    nom = forms.CharField(max_length=255, label=u"Nom")
    prenom = forms.CharField(max_length=255, label=u"Prénom")
    courriel = forms.CharField(max_length=255, label=u"Courriel")
    message = forms.CharField(label=u"Message", widget=forms.Textarea)
    #captcha = CaptchaField()


class RechercheEmployeForm(forms.Form):
    implantation = forms.ModelChoiceField(
        queryset=Implantation.ouvertes.all(), required=False)
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(), required=False)
    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(actif=True), required=False)
    mots = forms.CharField(max_length=100, required=False)

    def get_results(self):

        def is_int(val):
            try:
                return int(val)
            except:
                return None

        q = Q(actif=True)
        implantation_id = is_int(self.data.get('implantation', None))
        if implantation_id:
            q = q & Q(implantation__id=implantation_id)
        region_id = is_int(self.data.get('region', None))
        if region_id:
            q = q & Q(implantation__region__id=region_id)
        service_id = is_int(self.data.get('service', None))
        if service_id:
            q = q & Q(service__id=service_id)
        mots = [m for m in self.data.get('mots', '').split(' ') if m is not '']
        if len(mots) > 0:
            q_mots = Q()
            for m in mots:
                q_mots = q_mots | Q(nom__icontains=m) | Q(prenom__icontains=m) | Q(
                    fonction__icontains=m) | Q(service__nom__icontains=m)
            q = q & q_mots
        liste_employes = Employe.objects.filter(
            courriel__isnull=False).filter(q)
        return liste_employes


class EtablissementSearchForm(forms.Form):

    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, label="Par implantation régionale de l'AUF", empty_label="Toutes",
                                    help_text="")
    pays = forms.ModelChoiceField(queryset=Pays.objects.all(), required=False, label="Pays", empty_label="Tous",
                                  help_text="")

    def get_query_set(self):

        etablissements = Etablissement.objects
        if self.is_valid():
            query = self.cleaned_data['q']
            if query:
                etablissements = etablissements.search(query)
            titre = self.cleaned_data['titre']
            if titre:
                etablissements = etablissements.add_to_query('@titre ' + titre)
            discipline = self.cleaned_data['discipline']
            if discipline:
                etablissements = etablissements.filter_discipline(discipline)
            region = self.cleaned_data['region']
            if region:
                etablissements = etablissements.filter_region(region)
            type = self.cleaned_data['type']
            if type:
                etablissements = etablissements.filter_type(type)
            date_min = self.cleaned_data['date_min']
            if date_min:
                etablissements = etablissements.filter_debut(min=date_min)
            date_max = self.cleaned_data['date_max']
            if date_max:
                etablissements = etablissements.filter_debut(max=date_max)
        return etablissements.all()


class ActuSearchForm(forms.Form):

    region = forms.ModelChoiceField(queryset=Region.objects.all(
    ), required=False, label="Par implantation régionale de l'AUF", empty_label="Toutes", help_text="")
    titre = forms.CharField(max_length=255, required=False, label="Par titre")
    date_pub = forms.DateField(widget=forms.DateTimeInput(
        attrs={'class': 'datepicker'}), required=False, label="Par date de publication")


class EventSearchForm(forms.Form):

    region = forms.ModelChoiceField(queryset=Region.objects.all(
    ), required=False, label="Par implantation régionale de l'AUF", empty_label="Toutes", help_text="")
    date = forms.ChoiceField(label="Par type de date", required=False, help_text="", choices=(
        ('1', 'Événements à venir'), ('2', 'Événements passés')))
    titre = forms.CharField(max_length=255, required=False)


class BourseSearchForm(forms.Form):

    region = forms.ModelChoiceField(queryset=Region.objects.all(
    ), required=False, label="Par implantation régionale de l'AUF", empty_label="Toutes", help_text="")
    date = forms.ChoiceField(label="Par type de date", required=False, help_text="", choices=(
        ('1', 'Allocations en cours'), ('2', 'Allocations cloturées')))
    personna = forms.ModelChoiceField(label="Par public cible", required=False,
                                      empty_label="Sélectionnez un public...", help_text="", queryset=Personna.objects.all())
    titre = forms.CharField(max_length=255, required=False, label="Par titre")


class AppelSearchForm(forms.Form):

    region = forms.ModelChoiceField(queryset=Region.objects.all(
    ), required=False, label="Par implantation régionale de l'AUF", empty_label="Toutes", help_text="")
    date = forms.ChoiceField(label="Par type de date", required=False, help_text="", choices=(
        ('1', 'Appels d\'offres en cours'), ('2', 'Appels d\'offres clôturés')))
    personna = forms.ModelChoiceField(label="Par public cible", required=False,
                                      empty_label="Sélectionnez un public...", help_text="", queryset=Personna.objects.all())
    titre = forms.CharField(max_length=255, required=False, label="Par titre")


class AdressForm(forms.Form):

    email = forms.EmailField(label='email')
