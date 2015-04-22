# encoding: utf-8
from django.core.exceptions import ObjectDoesNotExist

from project.aldryn_search.base import AldrynIndexBase

from haystack import indexes

BUREAU_SLUGS = {
    '/bureau-ameriques/': u'Amériques',
    '/bureau-afrique-centrale-et-des-grands-lacs/': u'Afrique centrale et des Grands-Lacs',
    '/bureau-afrique-de-l-ouest/': u'Afrique de l\'Ouest',
    '/bureau-asie-pacifique/': u'Asie-Pacifique',
    '/bureau-caraibe/': u'Caraïbe',
    '/bureau-europe-centrale-et-orientale/': u'Europe centrale et orientale',
    '/bureau-europe-de-l-ouest/': u'Europe de l\'Ouest',
    '/bureau-moyen-orient/': u'Moyen-Orient',
    '/bureau-maghreb/': u'Maghreb',
    '/bureau-ocean-indien/': u'Océan Indien',
}


class AufIndex(AldrynIndexBase):
    index_title = True
    text = indexes.NgramField(document=True, use_template=False)
    title = indexes.NgramField(stored=True, indexed=False)
    description = indexes.NgramField(indexed=False, stored=True)
    bureaux = indexes.FacetMultiValueField(stored=True, null=True)
    annee = indexes.FacetField(stored=True, null=True)
    section = indexes.FacetField(stored=True, null=True)

    def prepare_bureaux(self, obj):
        try:
            return [b.nom for b in obj.page.bureauextension.bureau.all()]
        except ObjectDoesNotExist, e:
            for path in BUREAU_SLUGS.keys():
                if path in obj.page.get_absolute_url():
                    return [BUREAU_SLUGS[path]]
            return [u'Non précisé']

    def prepare_annee(self, obj):
        if obj.page.publication_date:
            return str(obj.page.publication_date.year)

    def prepare_section(self, obj):
        return obj.page.get_root().get_title()
