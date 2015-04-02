INSTALLED_APPS += (
    'auf.django.saml',
)

MIDDLEWARE_CLASSES += (
    'auf.django.saml.middleware.SPMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'auf.django.saml.backends.SPBackend',
)
