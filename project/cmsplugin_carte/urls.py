# encoding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'project.cmsplugin_carte.views',
    url(r'^pays.json', 'pays_json'),
)
