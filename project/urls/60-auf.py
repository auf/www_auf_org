# encoding: utf-8

from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView

from cms.sitemaps import CMSSitemap

urlpatterns += patterns('project.auf_site_institutionnel.views',
#    (r'^', include('project.carte.urls')),
    url(r'^cmsplugin_carte/', include('project.cmsplugin_carte.urls')),
    url(r'^offres_emploi/', include('project.offre_emploi.urls')),
#    url(r'^captcha/', include('captcha.urls')),
    url(r'^employes/$', 'employes', name='employes' ),
    url(r'^contacter/employe/(?P<employe_id>\d+)/$', 'contacter_employe', name='contacter_employe'),
    (r'^espace/', include('project.espace_membre.urls')),
#    (r'^$', 'accueil'),
    #Url articles
#    (r'^actualites/$', 'actualite'),
    (r'^actualites/(?P<slug>[-\w]+)/$', 'actualite_detail'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/actualites-regionales/(?P<slug>[-\w]+)/$', 'actualite_detail_br'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/veille-regionale/(?P<slug>[-\w]+)/$', 'veille_detail_br'),
    #(r'^allocations/$', 'bourse'),
    (r'^allocations/(?P<slug>[-\w]+)/$', 'bourse_detail'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/allocations-regionales/(?P<slug>[-\w]+)/$', 'bourse_detail_br'),
#    (r'^appels-offre/$', 'appel_offre'),
    (r'^appels-offre/(?P<slug>[-\w]+)/$', 'appel_offre_detail'),
    (r'^appels-offre-partenaires/$', 'appel_offre_partenaires'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/appels-offre-regionales/(?P<slug>[-\w]+)/$', 'appel_offre_detail_br'),
#    (r'^evenements/$', 'evenement'),
    (r'^evenements/(?P<slug>[-\w]+)/$', 'evenement_detail'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/evenements-regionales/(?P<slug>[-\w]+)/$', 'evenement_detail_br'),
#    (r'^publications/$', 'publication'),
    (r'^publications/(?P<slug>[-\w]+)/$', 'publication_detail'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/publications-regionales/(?P<slug>[-\w]+)/$', 'publication_detail_br'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/comares/(?P<slug>[-\w]+)/$', 'comares_detail'),

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


# Marc modul Upload
# urlpatterns += patterns ('',
#    url(r'^adminfiles/', include('adminfiles.urls')),
#)


# Mohamed
# Lien pour Contacte
#from contacts.views import contact
# urlpatterns += patterns('',
#    (r'^contact/$',contact),
#)

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

#Lien pour Newsletter
urlpatterns += patterns ('project.newsletter.views',
    (r'^lettre-information/(?P<id>[-\w]+)/$', 'newsletter'),
    (r'^lettre-information/$', 'newsletter_inscription'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/lettre-information-br/$', 'newsletter_inscription_br'),
    (r'^lettre-information-confirmation/$', 'newsletter_confirmation'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/lettre-information-confirmation-br/$', 'newsletter_confirmation_br'),
    (r'^lettre-information-desinscription/$', 'newsletter_desincription'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/lettre-information-desinscription/$', 'newsletter_desincription_br'),
    (r'^lettre-information-desinscription-confirme/$', 'newsletter_desincription_confirme'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/lettre-information-desinscription-confirme/$', 'newsletter_desincription_confirme_br'),
    (r'^lettre-information-desconfirmation/$', 'newsletter_desconfirmation'),
    (r'^bureau-(?P<slugRegion>[-\w]+)/lettre-information-desconfirmation/$', 'newsletter_desconfirmation_br'),
    (r'^fil-actualites/(?P<id>[-\w]+)/$', 'fil_actu'),
    (r'^planete-auf/(?P<id>[-\w]+)/$', 'planete'),
    (r'^breves/(?P<id>[-\w]+)/$', 'breve'),
)

#Lien pour contact
urlpatterns += patterns ('project.contacts.views',
    (r'^contact/$','contact'),
)

urlpatterns += patterns('',
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
)
