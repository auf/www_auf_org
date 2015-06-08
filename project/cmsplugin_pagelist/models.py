# -*- coding: utf-8 -*-

import os

from django.db import models
from cms.models.pluginmodel import CMSPlugin

from .lib.choices import (
    DynamicTemplateChoices,
    PageAttributeDynamicChoices,
)

TEMPLATE_PATH = os.path.join("cmsplugin_pagelist", "layouts")


class PageList(CMSPlugin):
    title = models.CharField("Titre", max_length="256")

    layout_template = models.CharField("Template utilisé pour l'affichage",
                                       choices=DynamicTemplateChoices(
                                           path=TEMPLATE_PATH,
                                           include='.html',
                                           exclude='default'), max_length=256,
                                       help_text="""Utiliser le template pour afficher le contenu de la liste""")

    root = models.ForeignKey("cms.Page", default=1,
                             help_text="""Selectionnez la page racine dont vous voulez afficher le contenu (liste des sous pages)""")

    nbelements = models.IntegerField(default=6,
                                     help_text="""Le nombre d'éléments à afficher ?""")
