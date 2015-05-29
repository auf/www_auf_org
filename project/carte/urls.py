from django.conf.urls import patterns, include, url

from django.views.generic.base import TemplateView

from .views import donnees_carte_json, test_carte

urlpatterns = patterns(
    '',
    url(r'^donnees_carte.json$', donnees_carte_json, name='donnees_carte'),
    url(r'^test/$', test_carte, name='test'),
)
