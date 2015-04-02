# encoding: utf-8
#Classe pour le flux RSS
from django.contrib.syndication.views import Feed
from project.auf_site_institutionnel.models import *
from auf.django.references.models import Region
from django.http import HttpResponseRedirect
from django.contrib.syndication.views import FeedDoesNotExist
from django.shortcuts import get_object_or_404
from itertools import chain
from django.utils.text import Truncator


class DerniereActualites(Feed):
    link = '/flux/actualite/'
    region_actuel = ''

    def get_object(self, request):
        region_actuel = request.GET.get('region_actuel', '')
        self.region_actuel = region_actuel
        if (self.region_actuel!=''):
            return Region.objects.get(nom = region_actuel)
        else:
            return Region.objects.get(nom = u'Ameriques')

    def title(self, obj):
        return "Actualite %s" % self.region_actuel

    def description(self, obj):
        return "Toutes les actualites %s" % self.region_actuel

    def items(self):
        if (self.region_actuel!=''):
            return Actualite.objects.filter(bureau=obj).filter(status=3).order_by('-date_pub')[:5]
        else:
            return Actualite.objects.all().filter(status=3).order_by('-date_pub')[:5]

    def item_title(self,obj):
        return "%s" % obj.titre

    def item_pubdate(self,obj):
        return obj.date_mod

    def item_description(self,obj):
        if (obj.resume!=''):
            return "%s"%(obj.resume)
        else:
            Truncator(obj.texte).chars(40)


class DerniereVeille(Feed):
    link = '/flux/veille/'
    region_actuel = ''

    def get_object(self, request):
        region_actuel = request.GET.get('region_actuel', '')
        self.region_actuel = region_actuel
        if (self.region_actuel!=''):
            return Region.objects.get(nom = region_actuel)
        else:
            return Region.objects.get(nom = u'Ameriques')

    def title(self, obj):
        return "Veille %s" % self.region_actuel

    def description(self, obj):
        return "Veille de la region %s" % self.region_actuel

    def items(self):
        if (self.region_actuel!=''):
            return Veille.objects.filter(bureau=obj).filter(status=3).order_by('-date_pub')[:5]
        else:
            return Veille.objects.all().filter(status=3).order_by('-date_pub')[:5]

    def item_title(self,obj):
        return "%s" % obj.titre

    def item_pubdate(self,obj):
        return obj.date_mod

    def item_description(self,obj):
        if (obj.resume!=''):
            return "%s"%(obj.resume)
        else:
            Truncator(obj.texte).chars(40)


class DerniereAppel(Feed):
    link = '/flux/appel_offre/'
    region_actuel = ''

    def get_object(self, request):
        region_actuel = request.GET.get('region_actuel', '')
        self.region_actuel = region_actuel
        if (self.region_actuel!=''):
            return Region.objects.get(nom = region_actuel)
        else:
            return Region.objects.get(nom = u'Ameriques')

    def title(self, obj):
        return "Appel d\'offres %s" % self.region_actuel

    def description(self, obj):
        return "Toutes les appels d\'offres %s" % self.region_actuel

    def items(self):
        if (self.region_actuel!=''):
            return Appel_Offre.objects.filter(bureau=obj).filter(status=3).order_by('-date_pub')[:5]
        else:
            return Appel_Offre.objects.all().filter(status=3).order_by('-date_pub')[:5]

    def item_title(self,obj):
        return "%s" % obj.titre

    def item_pubdate(self,obj):
        return obj.date_pub

    def item_description(self,obj):
        if (obj.resume!=''):
            return "%s"%(obj.resume)
        else:
            Truncator(obj.texte).chars(40)


class DerniereAllocations(Feed):
    link = '/flux/allocations/'
    region_actuel = ''

    def get_object(self, request):
        region_actuel = request.GET.get('region_actuel', '')
        self.region_actuel = region_actuel
        if (self.region_actuel!=''):
            return Region.objects.get(nom = region_actuel)
        else:
            return Region.objects.get(nom = u'Ameriques')

    def title(self, obj):
        return "allocations %s" % self.region_actuel

    def description(self, obj):
        return "Toutes les allocations %s" % self.region_actuel

    def items(self):
        if (self.region_actuel!=''):
            return Bourse.objects.filter(bureau=obj).filter(status=3).order_by('-date_pub')[:5]
        else:
            return Bourse.objects.all().filter(status=3).order_by('-date_pub')[:5]

    def item_title(self,obj):
        return "%s" % obj.titre

    def item_pubdate(self,obj):
        return obj.date_pub

    def item_description(self,obj):
        if (obj.resume!=''):
            return "%s"%(obj.resume)
        else:
            Truncator(obj.texte).chars(40)


class DerniereEvenement(Feed):
    link = '/flux/evenement/'
    region_actuel = ''

    def get_object(self, request):
        region_actuel = request.GET.get('region_actuel', '')
        self.region_actuel = region_actuel
        if (self.region_actuel!=''):
            return Region.objects.get(nom = region_actuel)
        else:
            return Region.objects.get(nom = u'Ameriques')

    def title(self, obj):
        return "Evenements %s" % self.region_actuel

    def description(self, obj):
        return "Tous les evenements %s" % self.region_actuel

    def items(self):
        if (self.region_actuel!=''):
            return Evenement.objects.filter(bureau=obj).filter(status=3).order_by('-date_pub')[:5]
        else:
            return Evenement.objects.all().filter(status=3).order_by('-date_pub')[:5]

    def item_title(self,obj):
        return "%s" % obj.titre

    def item_pubdate(self,obj):
        return obj.date_pub

    def item_description(self,obj):
        if (obj.resume!=''):
            return "%s"%(obj.resume)
        else:
            Truncator(obj.texte).chars(40)


class foad(Feed):
    link = '/flux/foad/'

    def title(self):
        return "RSS FOAD"

    def description(self):
        return "Tous les actus FOAD"

    def items(self):
	mot = ["FOAD", "TICE"]
	event = Evenement.objects.filter(titre__regex=r'(FOAD|TICE|CLOM|MOOC|Technologies|Formation à distance|Numérique|Innovation pédagogique)').order_by('-date_pub')[:4]
	actu = Actualite.objects.filter(titre__regex=r'(FOAD|TICE|CLOM|MOOC|Technologies|Formation à distance|Numérique|Innovation pédagogique)').order_by('-date_pub')[:6]
	appel = Appel_Offre.objects.filter(titre__regex=r'(FOAD|TICE|CLOM|MOOC|Technologies|Formation à distance|Numérique|Innovation pédagogique)').order_by('-date_pub')[:5]
	tout = chain(actu, appel, event)
        return tout

    def item_title(self,obj):
        return "%s" % obj.titre

    #def item_pubdate(self,obj):
        #return obj.date_pub

    def item_description(self,obj):
        if (obj.resume!=''):
            return "%s"%(obj.resume)
        else:
            return Truncator(obj.texte).chars(40)


class DernierePublication(Feed):
    link = '/flux/publication/'
    region_actuel = ''

    def get_object(self, request):
        region_actuel = request.GET.get('region_actuel', '')
        self.region_actuel = region_actuel
        if (self.region_actuel!=''):
            return Region.objects.get(nom = region_actuel)
        else:
            return Region.objects.get(nom = u'Ameriques')

    def title(self, obj):
        return "Publication %s" % self.region_actuel

    def description(self, obj):
        return "Toutes les publications %s" % self.region_actuel

    def items(self):
        if (self.region_actuel!=''):
            return Publication.objects.filter(bureau=obj).filter(status=3).order_by('-date_pub')[:5]
        else:
            return Publication.objects.all().filter(status=3).order_by('-date_pub')[:5]

    def item_title(self,obj):
        return "%s" % obj.titre

    def item_pubdate(self,obj):
        return obj.date_mod

    def item_description(self,obj):
        if (obj.resume!=''):
            return "%s"%(obj.resume)
        else:
            return Truncator(obj.texte).chars(40)
