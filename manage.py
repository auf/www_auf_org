#!/usr/bin/env python
import os
import sys

SITE_ROOT = os.path.dirname(__file__)

sys.path.append(os.path.join(SITE_ROOT, '../auf-django-sdk/sdk/django16_auf/'))
sys.path.append(os.path.join(SITE_ROOT, '../auf-django-sdk/sdk/django16_base/'))
sys.path.append(os.path.join(SITE_ROOT, '../auf-django-sdk/sdk/django16_dev/'))
sys.path.append(os.path.join(SITE_ROOT, '../auf-django-sdk/sdk/django16_auf_dev/'))
sys.path.append(os.path.join(SITE_ROOT, './packages/'))

if __name__ == "__main__":
    settings_module = "project.settings"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
