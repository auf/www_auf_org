# coding: utf8
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from auf.django.references.models import Region
from .models import *
from itertools import chain

from django.core.mail import send_mail


def newsletter(request, id, slugRegion=''):
    newsletter = get_object_or_404(Newsletter, id=id)
    list_bureau = newsletter.bureau.all()
    list_offre = newsletter.appel.all().order_by('-date_fin').reverse()[:7]
    list_evenement = newsletter.evenement.all()[:4]
    list_publi = newsletter.publication.all()[:4]
    list_actualite2 = newsletter.actualite.all()[:6]
    list_actualite = chain(list_actualite2, list_publi, list_evenement)
    return render_to_response('newsletter/lettre2.html', {'newsletter': newsletter, 'list_publi': list_publi, 'list_evenement': list_evenement, 'list_actualite': list_actualite, 'list_bureau': list_bureau, 'list_offre': list_offre}, context_instance=RequestContext(request))


def fil_actu(request, id):
    fil = get_object_or_404(Fil, id=id)
    list_actualite = fil.actualite.all()
    list_evenement = fil.evenement.all()
    return render_to_response('newsletter/fai.html', {'fil': fil, 'list_evenement': list_evenement, 'list_actualite': list_actualite}, context_instance=RequestContext(request))


def breve(request, id):
    breve = get_object_or_404(Breve, id=id)
    return render_to_response('newsletter/breves.html', {'breve': breve}, context_instance=RequestContext(request))


def planete(request, id):
    planete = get_object_or_404(Planete, id=id)
    list_offre = planete.appel_planete.all().order_by('-date_fin').reverse()
    list_bourse = planete.bourse_planete.all()
    list_evenement = planete.evenement_planete.all()
    list_all = chain(list_offre, list_bourse, list_evenement)
    fil = get_object_or_404(Fil, id=planete.fil_planete_id)
    list_actualite = fil.actualite.all()
    list_evenement2 = fil.evenement.all()
    list_projet = ProjetPlanete.objects.filter(
        planete=id).order_by('-ordre_projet')
    list_membre = MembrePlanete.objects.filter(
        planete=id).order_by('-ordre_membre')
    return render_to_response('newsletter/planete2.html', {'planete': planete, 'list_projet': list_projet, 'list_membre': list_membre, 'list_offre': list_all, 'list_actualite': list_actualite, 'list_evenement2': list_evenement2}, context_instance=RequestContext(request))


def newsletter_inscription(request):
    if request.method == 'POST':
        form = AbonneForm(request.POST)
        if form.is_valid():
            a = Abonne(adresse=form.cleaned_data['adresse'])
            a.save()
            a.bureau = [999]
            a.save()
            text_content = 'Votre abonnement à la lettre éléctronique de l\'AUF a été validé.'
            html_content = """
<p>Bonjour,</p>
<p>Votre inscription à la lettre électronique de l'AUF a bien été validée. Vous recevrez prochainement  les dernières informations de l'AUF dans votre boite de courriel électronique. Merci de votre intérêt.</p>
<p>Pour toutes informations complémentaires veuillez entrer en contact avec nous sur <a href="www.auf.org">www.auf.org</a></p>
"""
            msg = EmailMultiAlternatives('Inscription à la lettre éléctronique de l\'AUF',
                                         text_content, 'ne-pas-repondre@auf.org', [form.cleaned_data['adresse']])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('/lettre-information-confirmation/')
    else:
        form = AbonneForm()

    return render_to_response('newsletter/erreur-inscription.html', {'page_title': 'Inscription', 'abonne_form': form}, context_instance=RequestContext(request))


def newsletter_inscription_br(request, slugRegion):
    if request.method == 'POST':
        nb_region = get_object_or_404(Region, slug=slugRegion).id
        form = AbonneForm(request.POST)
        if form.is_valid():
            a = Abonne(adresse=form.cleaned_data['adresse'])
            a.save()
            a.bureau = [nb_region]
            a.save()
            text_content = 'Votre abonnement à la lettre éléctronique de l\'AUF a été validé.'
            html_content = '<p>Bonjour,</p><p>Votre inscription à la lettre éléctronique de l\'AUF a bien été validée. Vous recevrez prochainement les dernières informations de l\'AUF dans votre boite de courriers éléctroniques.</p><p>Pour toutes informations complémentaires veuillez contacter votre bureau régional à l\'adresse suivante: <a href="http://www.auf.org/auf_dans_le_monde/">www.auf.org/auf_dans_le_monde</a></p><p>Merci</p>'
            msg = EmailMultiAlternatives('Inscription à la lettre éléctronique de l\'AUF',
                                         text_content, 'ne-pas-repondre@auf.org', [form.cleaned_data['adresse']])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('/bureau-%s/lettre-information-confirmation-br/' % slugRegion)
    else:
        form = AbonneForm()

    return render_to_response('newsletter/erreur-inscription-br.html', {'page_title': 'Inscription', 'abonne_form': form}, context_instance=RequestContext(request))


def newsletter_confirmation(request, slugRegion=''):
    request.session['Region'] = slugRegion
    slugRegionContext = slugRegion
    context = RequestContext(request)
    list_news = Newsletter.objects.filter(status='3').order_by('-date')[:20]
    return render_to_response('newsletter/confirmation.html', {'page_title': 'Confirmation inscription', 'list_news': list_news}, context_instance=RequestContext(request))


def newsletter_confirmation_br(request, slugRegion=''):
    request.session['Region'] = slugRegion
    slugRegionContext = slugRegion
    context = RequestContext(request)
    region_actuel = context['region_actuel']
    list_news = Newsletter.objects.filter(
        bureau__slug=region_actuel).filter(status='3').order_by('-date')[:20]
    return render_to_response('newsletter/confirmation_br.html', {'page_title': 'Confirmation inscription', 'list_news': list_news}, context_instance=RequestContext(request))

# desinscription


def newsletter_desincription(request, slugRegion=''):
    return render_to_response('newsletter/desinscription.html', {'page_title': 'Désinscription', 'desabonne_form': DesinscireForm()}, context_instance=RequestContext(request))


def newsletter_desincription_br(request, slugRegion=''):
    return render_to_response('newsletter/desinscription-br.html', {'page_title': 'Désinscription', 'desabonne_form': DesinscireForm()}, context_instance=RequestContext(request))


def newsletter_desincription_confirme(request, slugRegion=''):
    if request.method == 'POST':
        form = DesinscireForm(request.POST)
        if form.is_valid():
            a = Abonne.objects.get(
                adresse=form.cleaned_data['adresse']).delete()
            send_mail('Désinscription à la lettre éléctronique de l\'AUF',
                      'Votre abonnement à la lettre éléctronique de l\'AUF a été résilié.', 'webmestre@auf.org', [form.cleaned_data['adresse']])
            return HttpResponseRedirect('/lettre-information-desconfirmation/')
    else:
        form = DesinscireForm()

    return render_to_response('newsletter/erreur-desinscription.html', {'page_title': 'Désinscription', 'desabonne_form': form}, context_instance=RequestContext(request))


def newsletter_desincription_confirme_br(request, slugRegion=''):
    if request.method == 'POST':
        form = DesinscireForm(request.POST)
        if form.is_valid():
            a = Abonne.objects.get(
                adresse=form.cleaned_data['adresse']).delete()
            send_mail('Désinscription à la lettre éléctronique de l\'AUF',
                      'Votre abonnement à la lettre éléctronique de l\'AUF a été résilié.', 'webmestre@auf.org', [form.cleaned_data['adresse']])
            return HttpResponseRedirect('/bureau-%s/lettre-information-desconfirmation/' % slugRegion)
    else:
        form = DesinscireForm()

    return render_to_response('newsletter/erreur-desinscription-br.html', {'page_title': 'Désinscription', 'desabonne_form': form}, context_instance=RequestContext(request))


def newsletter_desconfirmation(request, slugRegion=''):
    return render_to_response('newsletter/desconfirmation.html', {'page_title': 'Confirmation désinscription'}, context_instance=RequestContext(request))


def newsletter_desconfirmation_br(request, slugRegion=''):
    return render_to_response('newsletter/desconfirmation-br.html', {'page_title': 'Confirmation désinscription'}, context_instance=RequestContext(request))
