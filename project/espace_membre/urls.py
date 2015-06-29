# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('project.espace_membre.views',
    url(r'membre/$', 'accueil', name='espace_membre_accueil'),
    url(r'membre/modifier$', 'modifier', name='espace_membre_modifier'),
    url(r'membre/apercu$', 'apercu', name='espace_membre_apercu'),
    url(r'membre/valider$', 'valider', name='espace_membre_valider'),
    url(r'membre/connexion/(?P<token>\w+)$', 'connexion',
        name='espace_membre_connexion'),
)
