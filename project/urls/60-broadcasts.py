from django.conf.urls import patterns, include, url


urlpatterns += patterns('',
    url(r'^messages/', include('broadcasts.urls')),
)
