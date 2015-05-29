from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic.base import TemplateView
from auf_carte.carte.views import donnees_carte_json, test_carte

urlpatterns = patterns(
    '',
    url(r'^donnees_carte.json$', donnees_carte_json, name='donnees_carte'),
    url(r'^test/$', test_carte, name='test'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
