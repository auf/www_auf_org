import os

SITE_ID = '1'

PROJECT_ROOT = os.path.dirname(__file__)
ROOT = os.path.dirname(PROJECT_ROOT)

MEDIA_ROOT = os.path.join(ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT, 'sitestatic')
STATIC_URL = '/static/'

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'pagination',
    'tagging',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates/"),
)


