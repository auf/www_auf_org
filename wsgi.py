#!/usr/bin/env python
import os
import sys

# Pour le dev en local
sys.path.append('../auf-django-sdk/sdk/django17_auf/')
sys.path.append('../auf-django-sdk/sdk/django17_base/')
sys.path.append('../auf-django-sdk/sdk/django17_dev/')

# Pour la production
sys.path.append('/var/lib/auf-django-sdk/django17_auf/')
sys.path.append('/var/lib/auf-django-sdk/django17_base/')
sys.path.append('/var/lib/auf-django-sdk/django17_dev/')

sys.path.append('./project/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

