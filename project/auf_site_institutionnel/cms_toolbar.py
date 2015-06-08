# encoding: utf-8

from django.core.urlresolvers import reverse

from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from .models import (Bourse, Actualite, Veille, Appel_Offre, Evenement,
                     Publication)

MODEL_DICT = {
    'Actualite': 'Actualités',
    'Publication': 'Publications',
    'Appel_Offre': 'Appels d\'offre',
    'Bourse': 'Bourses',
    'Evenement': 'Événements',
    'Partenaire': 'Partenaires',
    'Comares': 'Comares',
    'Veille': 'Veilles',
}


@toolbar_pool.register
class AufToolbar(CMSToolbar):
    watch_models = [Bourse, Actualite, Veille, Appel_Offre, Evenement,
                    Publication]

    def populate(self):
        menu = self.toolbar.get_or_create_menu('auf-app', 'Ajouter un article')
        for m in self.watch_models:
            url = reverse('admin:auf_site_institutionnel' + '_' +
                          m._meta.object_name.lower() + "_add")
            menu.add_sideframe_item(MODEL_DICT[m._meta.object_name], url=url)
