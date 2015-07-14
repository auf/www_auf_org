# encoding: utf-8
import datetime

from django.core.exceptions import ObjectDoesNotExist
from haystack import indexes

from project.auf_site_institutionnel.models import \
    Bourse, Actualite, Appel_Offre, Evenement, Publication


class AufIndex(indexes.SearchIndex):
    text = indexes.NgramField(document=True, use_template=True)
    title = indexes.NgramField(model_attr='titre')
    bureaux = indexes.FacetMultiValueField(null=True, stored=True)
    annee = indexes.FacetField(stored=True, null=True)
    section = indexes.FacetField(stored=True, null=True)
    partenaire = indexes.FacetField(stored=True, null=True)
    date_pub = indexes.DateField(model_attr='date_pub', null=True)
    date_fin = indexes.DateField(model_attr='date_fin', null=True)

    def prepare_bureaux(self, obj):
        try:
            return [b.nom for b in obj.bureau.all()]
        except ObjectDoesNotExist as e:
            print(e)
            return [u'Non précisé']

    def prepare_annee(self, obj):
        if obj.date_pub is not None:
            return str(obj.date_pub.year)


class BourseIndex(AufIndex, indexes.Indexable):

    def get_model(self):
        return Bourse

    def prepare_section(self, obj):
        return u"Bourse"

    def prepare_date_pub(self, obj):
        return obj.date_pub.date()

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Bourse.objects.filter(status__in=[3, 5, 6])


class ActualiteIndex(AufIndex, indexes.Indexable):

    def get_model(self):
        return Actualite

    def prepare_section(self, obj):
        return u"Actualité"

    def index_queryset(self, using=None):
        return Actualite.objects.filter(status__in=[3, 5, 6])


class AppelOffreIndex(AufIndex, indexes.Indexable):
    partenaire = indexes.CharField(faceted=True, stored=True)

    def get_model(self):
        return Appel_Offre

    def prepare_section(self, obj):
        return u"Appel d\'offre"

    def prepare_partenaire(self, obj):
        if not obj.auf:
            return u'Partenaire'
        else:
            return u'AUF'

    def prepare_date_pub(self, obj):
        try:
            return obj.date_pub.date()
        except:
            return None

    def index_queryset(self, using=None):
        return Appel_Offre.objects.filter(status__in=[3, 5, 6])


class EvenementIndex(AufIndex, indexes.Indexable):

    def get_model(self):
        return Evenement

    def prepare_section(self, obj):
        return u"Événements"

    def prepare_date_pub(self, obj):
        try:
            return obj.date_pub.date()
        except:
            return None

    def index_queryset(self, using=None):
        return Evenement.objects.filter(status__in=[3, 5, 6])


class PublicationIndex(AufIndex, indexes.Indexable):

    def get_model(self):
        return Publication

    def prepare_section(self, obj):
        return u"Publication"

    def prepare_date_fin(self, obj):
        return datetime.date(2999, 1, 1)

    def index_queryset(self, using=None):
        return Publication.objects.filter(status__in=[3, 5, 6])
