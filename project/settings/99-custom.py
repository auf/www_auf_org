SESSION_COOKIE_NAME = 'sessionid_auf_org'

ROOT_URLCONF = 'project.urls'

INSTALLED_APPS += (
    'auf.django.references',
)

ALLOWED_HOSTS = ['www.auf.org']
THUMBNAIL_PROGRESSIVE = False


