# encoding: utf-8
from django.core.exceptions import ObjectDoesNotExist

from project.aldryn_search.base import AldrynIndexBase

from haystack import indexes

BUREAU_SLUGS = {
    '/bureau-ameriques/': 'Amériques',
    '/bureau-afrique-centrale-et-des-grands-lacs/': 'Afrique centrale et des Grands-Lacs',
    '/bureau-afrique-de-l-ouest/': 'Afrique de l\'Ouest',
    '/bureau-asie-pacifique/': 'Asie-Pacifique',
    '/bureau-caraibe/': 'Caraïbe',
    '/bureau-europe-centrale-et-orientale/': 'Europe centrale et orientale',
    '/bureau-europe-de-l-ouest/': 'Europe de l\'Ouest',
    '/bureau-moyen-orient/': 'Moyen-Orient',
    '/bureau-maghreb/': 'Maghreb',
    '/bureau-ocean-indien/': 'Océan Indien',
}


class AufIndex(AldrynIndexBase):
    index_title = True
    text = indexes.NgramField(document=True, use_template=False)
    title = indexes.NgramField(stored=True, indexed=False)
    description = indexes.NgramField(indexed=False, stored=True)
    bureaux = indexes.FacetMultiValueField(stored=True, null=True)
    annee = indexes.CharField(faceted=True, stored=True, null=True)
    section = indexes.FacetMultiValueField(stored=True)

    def prepare_bureaux(self, obj):
        try:
            return [b.nom for b in obj.page.bureauextension.bureau.all()]
        except ObjectDoesNotExist, e:
            for path in BUREAU_SLUGS.keys():
                if path in obj.page.get_absolute_url():
                    return BUREAU_SLUGS[path]
            return 'Non précisé'

    def prepare_annee(self, obj):
        if obj.page.publication_date:
            return str(obj.page.publication_date.year)

    def prepare_section(self, obj):
        return [obj.page.get_root().get_title()]
