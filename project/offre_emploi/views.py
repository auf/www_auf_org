# -*- encoding: utf-8 -*-
from .models import OffreEmploi
from django.shortcuts import render_to_response
from django.template import RequestContext


def offre_emploi_liste(request):
    offres_emploi = OffreEmploi.objects.all()
    var = {'offres_emploi': offres_emploi, 'page_title': 'Offre emploi'}
    return render_to_response("offre_emploi/liste_emplois.html", var,
                              RequestContext(request))
