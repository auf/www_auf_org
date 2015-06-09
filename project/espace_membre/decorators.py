# -*- encoding: utf-8 -*-

from django.shortcuts import redirect


def membre_connecte(fn):
    """ Vérifie si le membre est connecté avec son token dans la sesssion """
    def inner(request, *args, **kwargs):
        if 'espace_membre_etablissement' in request.session:
            return fn(request, *args, **kwargs)
        else:
            request.session['espace_membre_erreur'] = True
            return redirect('espace_membre_accueil')

    return inner
