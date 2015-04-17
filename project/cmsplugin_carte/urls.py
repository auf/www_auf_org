# encoding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'project.cmsplugin_carte.views',
    url(r'^pays.json', 'pays_json', name='cmsplugin_carte-pays_json'),
    url(r'^bureaux.json', 'bureaux_json', name='cmsplugin_carte-bureaux_json'),
)
