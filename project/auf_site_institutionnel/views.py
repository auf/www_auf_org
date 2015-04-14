# -*- coding: utf-8 -*-

import datetime

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse

from django.contrib import messages

from django.forms import ModelForm
from project.newsletter.models import AbonneForm

from project.auf_site_institutionnel.models import *
from filters import *

from project.auf_site_institutionnel.filters import MembreFilter, ImplantationFilter
from auf.django.references.models import Etablissement, Pays, Employe, Implantation, Region
from forms import *


#ACCUEIL et prout
def accueil(request):
    publi_list_accueil = Publication.objects.filter(status=3).order_by('-date_pub')[:6]
    event_list_accueil = Evenement.objects.filter(status=3).filter(date_fin__gte=datetime.datetime.now()).order_by('-date_fin').reverse()[:4]
    appel_list_accueil = list(Appel_Offre.objects.filter(status=3).filter(date_fin__gte=datetime.datetime.now()).order_by('-date_fin').reverse()[:2])
#    appel_list_accueil.insert(0, Appel_Offre.objects.get(id=2866))
    appel_list_accueil2 = Appel_Offre.objects.filter(status=3).filter(date_fin2__isnull = False)[:2]
    bourse_list_accueil = Bourse.objects.filter(status=3).filter(date_fin__gte=datetime.datetime.now()).order_by('-date_fin').reverse()[:3]
    bourse_list_accueil2 = Bourse.objects.filter(status=3).filter(date_fin2__isnull = False)[:2]
    abonne_form = AbonneForm()
    return render_to_response('Accueil.html', {'bourse_list_accueil': bourse_list_accueil, 'bourse_list_accueil2': bourse_list_accueil2, 'appel_list_accueil': appel_list_accueil, 'appel_list_accueil2': appel_list_accueil2, 'publi_list_accueil': publi_list_accueil, 'event_list_accueil': event_list_accueil, 'abonne_form': abonne_form, 'page_slug': ''}, context_instance = RequestContext(request))


#VUES ACTUALITES
def actualite(request):
    actualite = Actualite.objects
    if request.method == "POST":
        form = ActuSearchForm(request.POST)
        if form.is_valid():
            #PAR TITRE
            titre = form.cleaned_data['titre']
            if titre:
                actualite = actualite.filter(titre__icontains=titre)
            #PAR REGION
            region = form.cleaned_data['region']
            if region:
                actualite = actualite.filter(bureau__id=region.id)
            #PAR DATE
            date_pub = form.cleaned_data['date_pub']
            if date_pub:
                actualite = actualite.filter(date_pub=date_pub)
    else:
        form = ActuSearchForm()
    item_list = actualite.filter(status=3).order_by('-date_pub')
    return render_to_response('article.html', {'actualite_list': item_list, 'ActuSearchForm': form,  'nb_resultats': item_list.count(), 'page_slug': 'actualites/', 'page_title': 'Actualite'}, context_instance = RequestContext(request))


def actualite_latest(request, slugRegion=''):
    latest_actualite_list = Actualite.objects.all().order_by('-date_pub')[:5]
    return render_to_response('article.html', {'latest_actualite_list': latest_actualite_list}, context_instance = RequestContext(request))


def actualite_detail(request, slug):
    p = get_object_or_404(Actualite, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html', {'object':p, 'actualite': p, 'bureau': bureau, 'page_slug': 'actualites/', 'page_title': 'Actualite'}, context_instance = RequestContext(request))


def actualite_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion!=''):
        r = Region.objects.filter(slug=slugRegion)
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Actualite, slug=slug)
    return render_to_response('article.html', {'actualite': p, 'slugRegion': slugRegionContext, 'slugPersonna': slugPersonnaContext, 'page_slug': 'actualites/', 'page_title': 'Actualite'}, context_instance = RequestContext(request))


#VUES VEILLE REGIONALE
def veille_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion!=''):
        r = Region.objects.filter(slug=slugRegion)
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Veille, slug=slug)
    return render_to_response('article.html', {'actualite': p, 'slugRegion': slugRegionContext, 'slugPersonna': slugPersonnaContext, 'page_slug': 'actualites/', 'page_title': 'Actualite'}, context_instance = RequestContext(request))


#VUES BOURSES
def bourse(request):
    bourse = Bourse.objects
    if request.method == "POST":
        form = BourseSearchForm(request.POST)
        if form.is_valid():
            #PAR TITRE
            titre = form.cleaned_data['titre']
            if titre:
                bourse = bourse.filter(titre__icontains=titre)
            #PAR REGION
            region = form.cleaned_data['region']
            if region:
                bourse = bourse.filter(bureau__id=region.id)
            #PAR PERSONNA
            personna = form.cleaned_data['personna']
            if personna:
                bourse = bourse.filter(personna__id=personna.id)
            #PAR DATE
            date = form.cleaned_data['date']
            if date == "1":
                bourse = bourse.exclude(date_fin__lt=datetime.datetime.now())
            else:
                bourse = bourse.exclude(date_fin__gte=datetime.datetime.now())
    else:
        form = BourseSearchForm()
        bourse = bourse.exclude(date_fin__lt=datetime.datetime.now())
    item_list = bourse.filter(status=3).order_by('-date_fin').reverse()
    return render_to_response('article.html', {'bourse_list': item_list,  'BourseSearchForm': form, 'page_slug': 'allocations/', 'page_title': 'Allocations', 'nb_resultats': item_list.count()}, context_instance = RequestContext(request))


def bourse_latest(request, slugRegion=''):
    latest_bourse_list = Bourse.objects.all().order_by('-date_pub')[:5]
    return render_to_response('article.html', {'latest_bourse_list': latest_bourse_list}, context_instance = RequestContext(request))


def bourse_detail(request, slug):
    p = get_object_or_404(Bourse, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html', {'bourse': p, 'bureau': bureau, 'page_slug': 'allocations/', 'page_title': 'Allocations'}, context_instance = RequestContext(request))


def bourse_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion!=''):
        r = Region.objects.filter(slug=slugRegion)
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Bourse, slug=slug)
    return render_to_response('article.html', {'bourse': p, 'slugRegion': slugRegionContext, 'slugPersonna': slugPersonnaContext, 'page_slug': 'allocations/', 'page_title': 'Allocations'}, context_instance = RequestContext(request))


#VUES APPLE OFFRES
def appel_offre(request):
    appel = Appel_Offre.objects.filter(auf=True)
    if request.method == "POST":
        form = AppelSearchForm(request.POST)
        if form.is_valid():
            #PAR TITRE
            titre = form.cleaned_data['titre']
            if titre:
                appel = appel.filter(titre__icontains=titre)
            #PAR REGION
            region = form.cleaned_data['region']
            if region:
                appel = appel.filter(bureau__id=region.id)
            #PAR PERSONNA
            personna = form.cleaned_data['personna']
            if personna:
                appel = appel.filter(personna__id=personna.id)
            #PAR DATE
            date = form.cleaned_data['date']
            if date == "1":
                appel = appel.exclude(date_fin__lt=datetime.datetime.now())
            else:
                appel = appel.exclude(date_fin__gte=datetime.datetime.now())
    else:
        form = AppelSearchForm()
        appel = appel.exclude(date_fin__lt=datetime.datetime.now())
    item_list = appel.filter(status=3).exclude(date_fin2__isnull=True).order_by('-date_fin2').reverse()
    item_list3 = appel.filter(status=3).exclude(date_fin__isnull=True).order_by('-date_fin').reverse()
    return render_to_response('article.html', {'appel_offre_list': item_list, 'appel_offre_list2': item_list3,  'AppelSearchForm': form, 'page_slug': 'appels-offre/', 'page_title': 'Appels offres', 'nb_resultats': item_list.count(), 'nb_resultats2': item_list3.count()}, context_instance = RequestContext(request))


#VUES APPLE OFFRES PARTENAIRES
def appel_offre_partenaires(request):
    appel = Appel_Offre.objects.filter(auf=False)
    if request.method == "POST":
        form = AppelSearchForm(request.POST)
        if form.is_valid():
            #PAR TITRE
            titre = form.cleaned_data['titre']
            if titre:
                appel = appel.filter(titre__icontains=titre)
            #PAR REGION
            region = form.cleaned_data['region']
            if region:
                appel = appel.filter(bureau__id=region.id)
            #PAR PERSONNA
            personna = form.cleaned_data['personna']
            if personna:
                appel = appel.filter(personna__id=personna.id)
            #PAR DATE
            date = form.cleaned_data['date']
            if date == "1":
                appel = appel.exclude(date_fin__lt=datetime.datetime.now())
            else:
                appel = appel.exclude(date_fin__gte=datetime.datetime.now())
    else:
        form = AppelSearchForm()
        appel = appel.exclude(date_fin__lt=datetime.datetime.now())
    item_list = appel.filter(status=3).exclude(date_fin2__isnull=True).order_by('-date_fin2').reverse()
    item_list3 = appel.filter(status=3).exclude(date_fin__isnull=True).order_by('-date_fin').reverse()
    return render_to_response('article.html', {'appel_offre_list': item_list, 'appel_offre_list2': item_list3,  'AppelSearchForm': form, 'page_slug': 'appels-offre/', 'page_title': 'Appels offres', 'nb_resultats': item_list.count(), 'nb_resultats2': item_list3.count()}, context_instance = RequestContext(request))


def appel_offre_latest(request, slugRegion=''):
    latest_appel_offre_list = Appel_Offre.objects.all().order_by('-date_pub')[:5]
    return render_to_response('article.html', {'latest_appel_offre_list': latest_appel_offre_list}, context_instance = RequestContext(request))

def appel_offre_detail(request, slug):
    p = get_object_or_404(Appel_Offre, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html', {'appel_offre': p, 'bureau': bureau, 'page_slug': 'appels-offre/', 'page_title': 'Appels offres'}, context_instance = RequestContext(request))


def appel_offre_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion!=''):
        r = Region.objects.filter(slug=slugRegion)
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Appel_Offre, slug=slug)

    return render_to_response('article.html', {'appel_offre': p, 'slugRegion': slugRegionContext, 'slugPersonna': slugPersonnaContext, 'page_slug': 'appels-offre/', 'page_title': 'Appels offres'}, context_instance = RequestContext(request))


#VUES EVENEMENTS
def evenement(request):
    evenement = Evenement.objects
    if request.method == "POST":
        form = EventSearchForm(request.POST)
        if form.is_valid():
            #PAR TITRE
            titre = form.cleaned_data['titre']
            if titre:
                evenement = evenement.filter(titre__icontains=titre)
            #PAR REGION
            region = form.cleaned_data['region']
            if region:
                evenement = evenement.filter(bureau__id=region.id)
            #PAR DATE
            date = form.cleaned_data['date']
            if date == "1":
                evenement = evenement.filter(date_fin__gte=datetime.datetime.now())
            else:
                evenement = evenement.exclude(date_fin__gte=datetime.datetime.now())
    else:
        form = EventSearchForm()
        evenement = evenement.filter(date_fin__gte=datetime.datetime.now())
    item_list = evenement.filter(status=3).order_by('-date_fin').reverse()
    return render_to_response('article.html', {'evenement_list': item_list,  'EventSearchForm': form, 'page_slug': 'evenements/', 'page_title': 'Evenements', 'nb_resultats': item_list.count()}, context_instance = RequestContext(request))


def evenement_latest(request, slugRegion=''):
    latest_evenement_list = Evenement.objects.all().order_by('-date_pub')[:5]
    return render_to_response('article.html', {'latest_evenement_list': latest_evenement_list}, context_instance = RequestContext(request))


def evenement_detail(request, slug):
    p = get_object_or_404(Evenement, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html', {'evenement': p, 'bureau': bureau, 'page_slug': 'evenements/', 'page_title': 'Appels offres'}, context_instance = RequestContext(request))


def evenement_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion!=''):
        r = Region.objects.filter(slug=slugRegion)
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Evenement, slug=slug)
    return render_to_response('article.html', {'evenement': p, 'slugRegion': slugRegionContext, 'slugPersonna': slugPersonnaContext, 'page_slug': 'evenements/', 'page_title': 'Appels offres'}, context_instance = RequestContext(request))


#VUES PUBLICATION
def publication(request):
    dictFilter = {}
    item_list = PubliFilter(request.GET or None, queryset = Publication.objects.filter(**dictFilter).filter(status=3).order_by('-date_pub'))
    return render_to_response('article.html', {'publication_list': item_list,  'PubliForm': item_list.form, 'page_slug': 'publications/', 'page_title': 'Publications'}, context_instance = RequestContext(request))


def publication_latest(request, slugRegion=''):
    latest_publication_list = Publication.objects.all().order_by('-date_pub')[:5]
    return render_to_response('article.html', {'latest_publication_list': latest_publication_list}, context_instance = RequestContext(request))


def publication_detail(request, slug, slugRegion=''):
    p = get_object_or_404(Publication, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html', {'publication': p, 'bureau': bureau, 'page_slug': 'publications/', 'page_title': 'Publications'}, context_instance = RequestContext(request))


def publication_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion!=''):
        r = Region.objects.filter(slug=slugRegion)
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Publication, slug=slug)
    return render_to_response('article.html', {'publication': p, 'slugRegion': slugRegionContext, 'slugPersonna': slugPersonnaContext, 'page_slug': 'publications/', 'page_title': 'Publications'}, context_instance = RequestContext(request))


#VUE COMARES
def comares_detail(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion!=''):
        r = Region.objects.filter(slug=slugRegion)
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Comares, slug=slug)
    return render_to_response('article.html', {'comares': p, 'slugRegion': slugRegionContext, 'slugPersonna': slugPersonnaContext, 'page_slug': 'comares/', 'page_title': 'Actualités COMARES'}, context_instance = RequestContext(request))

#AUTRES VUES

def page_rss(request, slugRegion=''):
    return render_to_response('auf_site_institutionnel/page_rss.html', {'page_title': 'Actualite'}, context_instance = RequestContext(request))


def plan_du_site(request, slugRegion=''):
    return render_to_response('sitemap.html', {'page_title': 'Plan du site'}, context_instance = RequestContext(request))


def test_membres(request, slugRegion=''):
    dictFilter = {}
    if (slugRegion!=''):
        dictFilter['bureau__slug'] = slugRegion
    dictFilter['membre'] = True
    #if request.method == 'GET': # If the form has been submitted...
    item_list = MembreFilter(request.GET or None, queryset = Etablissement.objects.filter(**dictFilter))
    return render_to_response('auf_site_institutionnel/membre.html', {'page_title': 'Membres','membre_list': item_list,'form': item_list.form}, context_instance = RequestContext(request))


def employes(request, ):
    form = RechercheEmployeForm(request.GET)
    liste_employes = form.get_results()
    paginator = Paginator(liste_employes, 25)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        page  = paginator.page(page)
    except (EmptyPage, InvalidPage):
        page = paginator.page(paginator.num_pages)

    c = {'form' : form, 'page' : page,  }
    return render_to_response('auf_site_institutionnel/employes.html', Context(c), context_instance = RequestContext(request))

def contacter_employe(request, employe_id=None):
    employe = get_object_or_404(Employe, id=employe_id)

    # certains employés n'ont pas de courriels
    if employe.courriel is None:
        messages.warning(request, u"%s n'a pas de courriel" % employe)
        return redirect('employes')

    if request.method == "POST":
        form = ContactEmployeForm(request.POST)
        if form.is_valid():
            from django.core.mail import send_mail
            sujet = u"%s %s vous contacte de www.auf.org" % (form.data.get('nom'), form.data.get('prenom'),)
            message = form.data.get('message')
            expediteur = form.data.get('courriel')
            destinataire = [employe.courriel, ]
            send_mail(sujet, message, expediteur, destinataire, )
            return redirect('employes')
    else:
        form = ContactEmployeForm()
    c = {'form' : form, 'employe' : employe}
    return render_to_response('auf_site_institutionnel/contacter_employe.html', Context(c), context_instance = RequestContext(request))


def membre(request, slugRegion=''):
    context = RequestContext(request)
    dictFilter = {}
    if (slugRegion!=''):
        dictFilter['bureau__slug'] = slugRegion
    dictFilter['membre'] = True
    item_list = MembreFilter(request.GET or None, queryset = Etablissement.objects.filter(**dictFilter))

    return render_to_response('article.html', {'form': item_list.form, 'membre_list': item_list, 'page_title': 'Liste des membres'}, context_instance = RequestContext(request))


def implantation(request):
    dictFilter = {}
    dictFilter['actif'] = True
    item_list = ImplantationFilter(request.GET or None, queryset = Implantation.ouvertes.filter(**dictFilter))
    
    return render_to_response('auf_site_institutionnel/implantation.html', {'form': item_list.form,  'implantation_list': item_list, 'page_title': 'Liste des implantations'}, context_instance = RequestContext(request))

def membre_detail(request, id, slugRegion=''):
    p = Etablissement.objects.filter(id=id)
    return render_to_response('auf_site_institutionnel/membre_detail.html', {'membre': p,'page_title': 'Membres'}, context_instance = RequestContext(request))


def implantation_detail(request, id, slugRegion=''):
    p = Implantation.objects.filter(id=id)
    return render_to_response('auf_site_institutionnel/implantation_detail.html', {'implantation': p,'page_title': 'Implantation'}, context_instance = RequestContext(request))
