try:
    from django.conf.urls.defaults import patterns, include, \
        handler500, handler404, url
except ImportError:
    from django.conf.urls import patterns, include, \
        handler500, handler404, url

from django.contrib import admin

handler404
handler500 # Pyflakes

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/', include(admin.site.urls)),
)
