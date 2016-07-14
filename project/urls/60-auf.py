# encoding: utf-8

from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView

from cms.sitemaps import CMSSitemap

urlpatterns += patterns('project.auf_site_institutionnel.views',
#    (r'^', include('project.carte.urls')),
    url(r'^cmsplugin_carte/', include('project.cmsplugin_carte.urls')),
    url(r'^employes/$', 'employes', name='employes' ),
    url(r'^contacter/employe/(?P<employe_id>\d+)/$', 'contacter_employe', name='contacter_employe'),
    url(r'^espace/', include('project.espace_membre.urls')),

    #Url articles
    (r'^actualites/(?P<slug>[-\w]+)/$', 'actualite_detail'),
    (r'^bureau/bureau-(?P<slugRegion>[-\w]+)/actualites-regionales/(?P<slug>[-\w]+)/$', 'actualite_detail_br'),
    (r'^veille/(?P<slug>[-\w]+)/$', 'veille_detail'),
    (r'^bureau/bureau-(?P<slugRegion>[-\w]+)/veille-regionale/(?P<slug>[-\w]+)/$', 'veille_detail_br'),

    (r'^allocations/(?P<slug>[-\w]+)/$', 'bourse_detail'),
    (r'^bureau/bureau-(?P<slugRegion>[-\w]+)/allocations-regionales/(?P<slug>[-\w]+)/$', 'bourse_detail_br'),
    (r'^appels-offre/(?P<slug>[-\w]+)/$', 'appel_offre_detail'),
    (r'^bureau/bureau-(?P<slugRegion>[-\w]+)/appels-offre-regionales/(?P<slug>[-\w]+)/$', 'appel_offre_detail_br'),
    (r'^evenements/(?P<slug>[-\w]+)/$', 'evenement_detail'),
    (r'^bureau/bureau-(?P<slugRegion>[-\w]+)/evenements-regionales/(?P<slug>[-\w]+)/$', 'evenement_detail_br'),
    (r'^publications/(?P<slug>[-\w]+)/$', 'publication_detail'),
    (r'^bureau/bureau-(?P<slugRegion>[-\w]+)/publications-regionales/(?P<slug>[-\w]+)/$', 'publication_detail_br'),

    #Fin url artcile
    (r'^membres/$', 'membre'),
    (r'^accueil/membres/$', 'membre'),
    (r'^membres/(?P<id>[-\w]+)/$', 'membre_detail'),
    (r'^implantations/$', 'implantation'),
    (r'^implantations/(?P<id>[-\w]+)/$', 'implantation_detail'),
    (r'^(?P<slugRegion>[-\w]+)/membres/$', 'membre'),
    (r'^rss/$', 'page_rss'),
    (r'^plan-du-site/$', 'plan_du_site'),
    (r'^nos-membres/$', 'test_membres'),

)

from feeds import *

urlpatterns += patterns ('',
    (r'^flux/actualite/$', DerniereActualites()),
    (r'^flux/appel_offre/$', DerniereAppel()),
    (r'^flux/allocations/$', DerniereAllocations()),
    (r'^flux/bourse/$', DerniereAllocations()),
    (r'^flux/evenement/$', DerniereEvenement()),
    (r'^flux/publication/$', DernierePublication()),
    (r'^flux/veille/$', DerniereVeille()),
    (r'^flux/foad/$', foad()),
)

#Lien pour contact
urlpatterns += patterns ('project.contacts.views',
    (r'^contact/$','contact'),
)

urlpatterns += patterns('',
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
)
