from django.conf.urls import patterns, include, url


urlpatterns += patterns('',
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
)
