# -*- coding: utf-8 -*-

import os

from django.db import models
from cms.models.pluginmodel import CMSPlugin

from auf.django.references.models import Region

from .lib.choices import DynamicTemplateChoices

TEMPLATE_PATH = os.path.join("cmsplugin_modellist", "layouts")
MODEL_LIST = (
    ('Actualite', 'Actualités'),
    ('Publication', 'Publications'),
    ('Appel_Offre', 'Appels d\'offre'),
    ('Bourse', 'Bourses'),
    ('Evenement', 'Événements'),
    ('Partenaire', 'Partenaires'),
    ('Comares', 'Comares'),
    ('Veille', 'Veilles'),
)


class ModelList(CMSPlugin):
    title = models.CharField("Titre", max_length="256")

    bureau = models.ManyToManyField(Region, related_name="cmsplugin_modellist_bureau")

    layout_template = \
        models.CharField("Template utilisé pour l'affichage",
            choices = DynamicTemplateChoices(
                path=TEMPLATE_PATH,
                include='.html',
                exclude='default'),
            max_length=256,
            help_text="""Utiliser le template pour afficher le contenu de la liste""")

    modele = models.CharField("Modèle", choices=MODEL_LIST, max_length="256",
      help_text="""Selectionnez la page racine dont vous voulez afficher le contenu (liste des sous pages)""")

    nbelements = models.IntegerField(default=6,
      help_text="""Le nombre d'éléments à afficher ?""")

    def copy_relations(self, oldinstance):
        self.bureau = oldinstance.bureau.all()
