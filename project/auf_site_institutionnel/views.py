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

BUREAUX_CODE = {
    'ameriques': 'A',
    'afrique-centrale-et-des-grands-lacs': 'ACGL',
    'afrique-de-l-ouest': 'AO',
    'asie-pacifique': 'AP',
    'caraibe': 'C',
    'europe-centrale-et-orientale': 'ECO',
    'europe-de-l-ouest': 'EO',
    'moyen-orient': 'MO',
    'maghreb': 'M',
    'ocean-indien': 'OI',
}


def actualite_detail(request, slug):
    p = get_object_or_404(Actualite, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html',
                              {'object': p,
                               'actualite': p,
                               'bureau': bureau,
                               'page_slug': 'actualites/',
                               'page_title': 'actualite'},
                              context_instance=RequestContext(request))


def actualite_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion != ''):
        r = Region.objects.filter(code=BUREAUX_CODE[slugRegion])
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Actualite, slug=slug)
    return render_to_response('article.html',
                              {'object': p,
                               'slugRegion': slugRegionContext,
                               'slugPersonna': slugPersonnaContext,
                               'page_slug': 'actualites/',
                               'page_title': 'actualite'},
                              context_instance=RequestContext(request))


# VUES VEILLE REGIONALE
def veille_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion != ''):
        r = Region.objects.filter(code=BUREAUX_CODE[slugRegion])
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Veille, slug=slug)
    return render_to_response('article.html',
                              {'object': p,
                               'slugRegion': slugRegionContext,
                               'slugPersonna': slugPersonnaContext,
                               'page_slug': 'actualites/',
                               'page_title': 'veille'},
                              context_instance=RequestContext(request))


def bourse_detail(request, slug):
    p = get_object_or_404(Bourse, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html',
                              {'object': p,
                               'bureau': bureau,
                               'page_slug': 'allocations/',
                               'page_title': 'appel_offre'},
                              context_instance=RequestContext(request))


def bourse_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion != ''):
        r = Region.objects.filter(code=BUREAUX_CODE[slugRegion])
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Bourse, slug=slug)
    return render_to_response('article.html',
                              {'object': p,
                               'slugRegion': slugRegionContext,
                               'slugPersonna': slugPersonnaContext,
                               'page_slug': 'allocations/',
                               'page_title': 'appel_offre'},
                              context_instance=RequestContext(request))


def appel_offre_detail(request, slug):
    p = get_object_or_404(Appel_Offre, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html',
                              {'object': p,
                               'bureau': bureau,
                               'page_slug': 'appels-offre/',
                               'page_title': 'appel_offre'},
                              context_instance=RequestContext(request))


def appel_offre_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion != ''):
        r = Region.objects.filter(code=BUREAUX_CODE[slugRegion])
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Appel_Offre, slug=slug)

    return render_to_response('article.html',
                              {'object': p,
                               'slugRegion': slugRegionContext,
                               'slugPersonna': slugPersonnaContext,
                               'page_slug': 'appels-offre/',
                               'page_title': 'appel_offre'},
                              context_instance=RequestContext(request))


def evenement_detail(request, slug):
    p = get_object_or_404(Evenement, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html',
                              {'object': p,
                               'bureau': bureau,
                               'page_slug': 'evenements/',
                               'page_title': 'evenement'},
                              context_instance=RequestContext(request))


def evenement_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion != ''):
        r = Region.objects.filter(code=BUREAUX_CODE[slugRegion])
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Evenement, slug=slug)
    return render_to_response('article.html',
                              {'object': p,
                               'slugRegion': slugRegionContext,
                               'slugPersonna': slugPersonnaContext,
                               'page_slug': 'evenements/',
                               'page_title': 'evenement'},
                              context_instance=RequestContext(request))


def publication_detail(request, slug, slugRegion=''):
    p = get_object_or_404(Publication, slug=slug)
    bureau = ', '.join([b.nom for b in p.bureau.all()])
    return render_to_response('article.html',
                              {'object': p,
                               'bureau': bureau,
                               'page_slug': 'publications/',
                               'page_title': 'publication'},
                              context_instance=RequestContext(request))


def publication_detail_br(request, slug, slugRegion=''):
    slugRegionContext = ''
    slugPersonnaContext = ''
    if (slugRegion != ''):
        r = Region.objects.filter(code=BUREAUX_CODE[slugRegion])
        if (not r):
            slugPersonnaContext = '/' + slugRegion
        slugRegionContext = '/' + slugRegion
    p = get_object_or_404(Publication, slug=slug)
    return render_to_response('article.html',
                              {'object': p,
                               'slugRegion': slugRegionContext,
                               'slugPersonna': slugPersonnaContext,
                               'page_slug': 'publications/',
                               'page_title': 'publication'},
                              context_instance=RequestContext(request))

# AUTRES VUES


def page_rss(request, slugRegion=''):
    return render_to_response('auf_site_institutionnel/page_rss.html',
                              {'page_title': 'Actualite'},
                              context_instance=RequestContext(request))


def plan_du_site(request, slugRegion=''):
    return render_to_response('sitemap.html',
                              {'page_title': 'Plan du site'},
                              context_instance=RequestContext(request))


def test_membres(request, slugRegion=''):
    dictFilter = {}
    if (slugRegion != ''):
        dictFilter['bureau__slug'] = slugRegion
    dictFilter['membre'] = True
    # if request.method == 'GET': # If the form has been submitted...
    item_list = MembreFilter(
        request.GET or None,
        queryset=Etablissement.objects.filter(
            **dictFilter))
    return render_to_response(
        'auf_site_institutionnel/membre.html',
        {
            'page_title': 'Membres',
            'membre_list': item_list,
            'form': item_list.form},
        context_instance=RequestContext(request))


def employes(request, ):
    form = RechercheEmployeForm(request.GET)
    liste_employes = form.get_results()
    paginator = Paginator(liste_employes, 25)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        page = paginator.page(paginator.num_pages)

    c = {'form': form, 'page': page, }
    return render_to_response(
        'auf_site_institutionnel/employes.html',
        Context(c),
        context_instance=RequestContext(request))


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
            sujet = u"%s %s vous contacte de www.auf.org" % (
                form.data.get('nom'), form.data.get('prenom'),)
            message = form.data.get('message')
            expediteur = form.data.get('courriel')
            destinataire = [employe.courriel, ]
            send_mail(sujet, message, expediteur, destinataire, )
            return redirect('employes')
    else:
        form = ContactEmployeForm()
    c = {'form': form, 'employe': employe}
    return render_to_response(
        'auf_site_institutionnel/contacter_employe.html',
        Context(c),
        context_instance=RequestContext(request))


def membre(request, slugRegion=''):
    context = RequestContext(request)
    dictFilter = {}
    if (slugRegion != ''):
        dictFilter['bureau__slug'] = slugRegion
    dictFilter['membre'] = True
    item_list = MembreFilter(
        request.GET or None,
        queryset=Etablissement.objects.filter(
            **dictFilter))

    return render_to_response(
        'auf_site_institutionnel/membre.html',
        {
            'form': item_list.form,
            'membre_list': item_list,
            'page_title': 'Liste des membres'},
        context_instance=RequestContext(request))


def implantation(request):
    dictFilter = {}
    dictFilter['actif'] = True
    item_list = ImplantationFilter(
        request.GET or None,
        queryset=Implantation.ouvertes.filter(
            **dictFilter))

    return render_to_response(
        'auf_site_institutionnel/implantation.html',
        {
            'form': item_list.form,
            'implantation_list': item_list,
            'page_title': 'Liste des implantations'},
        context_instance=RequestContext(request))


def membre_detail(request, id, slugRegion=''):
    p = Etablissement.objects.filter(id=id)
    return render_to_response(
        'auf_site_institutionnel/membre_detail.html',
        {
            'membre': p,
            'page_title': 'Membres'},
        context_instance=RequestContext(request))


def implantation_detail(request, id, slugRegion=''):
    p = Implantation.objects.filter(id=id)
    return render_to_response(
        'auf_site_institutionnel/implantation_detail.html',
        {
            'implantation': p,
            'page_title': 'Implantation'},
        context_instance=RequestContext(request))
