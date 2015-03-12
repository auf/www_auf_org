# encoding: utf-8

from aldryn_search.base import AldrynIndexBase

from haystack import indexes

from project.djangocms_bureaux.models import DoesNotExist


class AufIndex(AldrynIndexBase):
    index_title = True
    text = indexes.NgramField(document=True, use_template=False)
    title = indexes.NgramField(stored=True, indexed=False)
    description = indexes.NgramField(indexed=False, stored=True, null=True)
    bureaux = indexes.FacetMultiValueField(null=True)
    annee = indexes.IntegerField(faceted=True)
    section = indexes.CharField(faceted=True)

    def prepare_bureaux(self, obj):
        try:
            return [b.nom for b in obj.page.bureauextension.bureau.all()]
        except DoesNotExist, e:
            print(e)
            return 'Non précisé'

    def prepare_annee(self, obj):
        return obj.page.publication_date.year

    def prepare_section(self, obj):
        return obj.page.get_root().get_title()
