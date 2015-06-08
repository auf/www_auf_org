from auf.django.saml import settings as saml_settings

urlpatterns += patterns(
    '',
    (r'^', include('auf.django.saml.urls')),
)

if not saml_settings.SAML_AUTH:
    urlpatterns += patterns('',
        (r'^', include('auf.django.saml.mellon_urls')),
    )
