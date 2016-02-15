from django.db import models
from cms.models.pluginmodel import CMSPlugin


class MailmanPluginModel(CMSPlugin):
    titre = models.CharField(max_length=100)
    liste = models.CharField(max_length=100)
