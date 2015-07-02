# -=- encoding: utf-8 -=-
import collections

import unittest
import .models
import .views
import auf.django.references.models as auf_refs


class DonneesPaysTest(unittest.TestCase):
    def setUp(self):
        self.pays = [auf_refs.Pays(id=1, code='AF', code_iso3='AFG'),
                     auf_refs.Pays(id=2, code='FR', code_iso3='FRA'),
                     auf_refs.Pays(id=3, code='EN', code_iso3='ENG'),
                     auf_refs.Pays(id=4, code='CA', code_iso3='CAN'), ]
        self.etablissements = [
            auf_refs.Etablissement(pays=self.pays[0]),
            auf_refs.Etablissement(pays=self.pays[1]),
            auf_refs.Etablissement(pays=self.pays[1]),
        ]
        self.impl_cnfp = auf_refs.Implantation(
            id=4, adresse_postale_pays=self.pays[2], type=views.TYPE_CNFP)
        self.implantations_non_cnfp = [
            auf_refs.Implantation(id=1, adresse_postale_pays=self.pays[1],
                                  type=views.TYPE_SIEGE),
            auf_refs.Implantation(id=2, adresse_postale_pays=self.pays[2],
                                  type=views.TYPE_ANTENNE),
            auf_refs.Implantation(id=3, adresse_postale_pays=self.pays[2],
                                  type=views.TYPE_BUREAU), ]
        self.implantations = self.implantations_non_cnfp + [self.impl_cnfp]
        self.donnees_pays = views.get_donnees_pays(
            self.etablissements, self.implantations, self.pays)

    def test_donnees_pays_keys(self):
        """ Tous les pays sont dans le dictionnaire donnees_pays, même ceux qui
        n'ont pas de membres AUF. """
        self.assertEqual(set(self.donnees_pays.iterkeys()),
                         set(pays.code_iso3 for pays in self.pays))

    def test_etablissements_par_pays_counter(self):
        counter = views.get_etablissements_par_pays_counter(self.etablissements)
        self.assertEqual(counter, {self.pays[0]: 1, self.pays[1]: 2})

    def test_get_implantations_par_pays(self):
        par_pays = views.get_implantations_par_pays(self.implantations)
        self.assertEqual(set(par_pays.iterkeys()),
                         {i.adresse_postale_pays.code
                          for i in self.implantations_non_cnfp})
        self.assertFalse(
            [i for i in par_pays[self.impl_cnfp.adresse_postale_pays.code]
             if i['id'] == self.impl_cnfp.id])
        self.assertEqual([i['id'] for i in par_pays[self.pays[2].code]],
                         [3, 2])

    def test_sort_implantations(self):
        self.assertEqual(views.sort_implantations(self.implantations_non_cnfp),
                         [self.implantations_non_cnfp[0],
                          self.implantations_non_cnfp[2],
                          self.implantations_non_cnfp[1]])

FakeCoords = collections.namedtuple('FakeCoords',
                                    ('latitude', 'longitude', 'implantation'))

FakeImplantation = collections.namedtuple(
    'FakeImplantation', ('id', 'nom', 'adresse_physique_ville'))


class LieuxImplantationsTest(unittest.TestCase):
    def setUp(self):
        self.implantations = {
            'cnf_bamako': FakeImplantation(id=1, nom='CNF Bamako',
                                           adresse_physique_ville='Bamako'),
            'bureau_bamako': FakeImplantation(id=2, nom='Bureau Bamako',
                                              adresse_physique_ville='Bamako'),
            'bureau_paris': FakeImplantation(id=3, nom='Bureau Paris',
                                             adresse_physique_ville='Paris'),
        }

        self.coords = [
            FakeCoords(latitude=1, longitude=1,
                       implantation=self.implantations['cnf_bamako']),
            FakeCoords(latitude=1, longitude=1,
                       implantation=self.implantations['bureau_bamako']),
            FakeCoords(latitude=2, longitude=2,
                       implantation=self.implantations['bureau_paris']),
        ]
        self.lieux = views.get_lieux_implantations(self.coords)

    def test_nb_lieux(self):
        self.assertEqual(len(self.lieux), 2)

    def test_coords(self):
        self.assertEqual(set((c.latitude, c.longitude) for c in self.coords),
                         {(1, 1), (2, 2)})

    def test_nb_implantations(self):
        self.assertEqual(
            {l['nom']: len(l['implantations']) for l in self.lieux},
            {'Bamako': 2, 'Paris': 1})