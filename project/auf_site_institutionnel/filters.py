# -*- encoding: utf-8 -*-
from django.conf import settings
from project.auf_site_institutionnel.models import Publication
from auf.django.references.models import Etablissement, Implantation, Pays, Region
import django_filters


class MembreFilter(django_filters.FilterSet):
    region = django_filters.ModelChoiceFilter(
        label="Par implantation régionale de l'AUF",
        empty_label="Sélectionnez une région...",
        queryset=Region.objects.all())
    pays = django_filters.ModelChoiceFilter(
        label="Par Pays",
        empty_label="Sélectionnez un pays...",
        queryset=Pays.objects.all())
    statut = django_filters.ChoiceFilter(
        label="Par statut de membre",
        required=False,
        choices=(
            ('',
             'Sélectionnez un statut...'),
            ('T',
             'Membre Titulaire'),
            ('A',
             'Membre associé')))
    #qualite = django_filters.ChoiceFilter(label="Par type de membre", required=False, choices=(('', 'Sélectionnez un type...'), ('ESR', 'Établissement'), ('RES', 'Réseaux institutionnels'), ('CIR', 'Réseaux d administrateurs')))
    nom = django_filters.CharFilter(lookup_type='icontains', name='nom')

    class Meta:
        model = Etablissement
        fields = ['pays', 'region', 'statut', 'nom']


class ImplantationFilter(django_filters.FilterSet):
    region = django_filters.ModelChoiceFilter(
        label="Région", empty_label="Toutes", queryset=Region.objects.all())
    #pays = django_filters.ModelChoiceFilter(label="Pays", empty_label="Tous", queryset= Pays.objects.all())
    type = django_filters.ChoiceFilter(
        label="Type", required=False, choices=[
            ('', '-----------')] + [
            (x, x) for x in list(
                set(
                    Implantation.ouvertes.values_list(
                        'type', flat=True)))])

    class Meta:
        model = Implantation
        fields = ['region', 'type']


class PubliFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(lookup_type='icontains', name='titre')
    bureau = django_filters.ModelChoiceFilter(
        label="Par implantation régionale de l'AUF",
        empty_label="Sélectionnez une région...",
        queryset=Region.objects.all())
    #date = django_filters.ChoiceFilter(label="Par type de date", required=False, choices=(('', 'Sélectionnez un type...'), ('1', 'Bourses permanente'), ('2', 'Bourses en cours'), ('2', 'Bourses cloturés')))

    class Meta:
        model = Publication
        fields = ['bureau', 'titre']
