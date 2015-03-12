#!/usr/bin/env python
import os
import sys

SITE_ROOT = os.path.dirname(__file__)

# Pour le dev en local
sys.path.append(os.path.join(SITE_ROOT, '../auf-django-sdk/sdk/django16_auf/'))
sys.path.append(os.path.join(SITE_ROOT, '../auf-django-sdk/sdk/django16_base/'))
sys.path.append(os.path.join(SITE_ROOT, '../auf-django-sdk/sdk/django16_dev/'))

# Pour la production
sys.path.append('/var/lib/auf-django-sdk/django16_auf/')
sys.path.append('/var/lib/auf-django-sdk/django16_base/')
sys.path.append('/var/lib/auf-django-sdk/django16_dev/')

sys.path.append(SITE_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

