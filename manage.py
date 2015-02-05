#!/usr/bin/env python
import os
import sys

sys.path.append('../auf-django-sdk/sdk/django17_auf/')
sys.path.append('../auf-django-sdk/sdk/django17_base/')
sys.path.append('../auf-django-sdk/sdk/django17_auf_dev/')
sys.path.append('./project/')

if __name__ == "__main__":
    settings_module = "settings"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
