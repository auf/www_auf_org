# -*- coding: utf-8 -*-

import os

from django.db import models
from cms.models.pluginmodel import CMSPlugin


class MailmanPluginModel(CMSPlugin):
    titre = models.CharField(max_length=100)
    liste = models.CharField(max_length=100)
    layout_template = models.CharField("Template utilisé pour l'affichage",
                                       max_length=256,
                                       help_text="""Utiliser le template pour afficher le contenu de la liste""")

