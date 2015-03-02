# -*- encoding: utf-8 -*

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cms30',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = 'ilseraitsagedemodifiercetteclefpourquelquechosedautre.'

RAVEN_CONFIG = {
    'dsn': '',
}

SAML_AUTH = False

# Optionnel
PIWIK_TOKEN = None

DEBUG = True
AUF_REFERENCES_MANAGED = True

