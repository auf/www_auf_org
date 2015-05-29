# -=- encoding: utf-8 -=-
import codecs
import collections
import itertools
import json
import os
import django.http
import django.shortcuts
import auf.django.references.models as auf_refs
from auf_carte.carte import models

TYPE_SIEGE = u'Siège'
TYPE_CNFP = u'Campus numérique francophone partenaire'
TYPE_SERVICE_CENTRAL = u'Service central'
TYPE_INSTITUT = u'Institut'
TYPE_BUREAU = u'Bureau'
TYPE_ANTENNE = u'Antenne'
TYPE_CNF = u'Campus numérique francophone'
TYPE_CAI = u'Centre d\'accès à l\'information'


ORDRE_TYPES_IMPLANTATIONS = dict((type_, i) for i, type_ in enumerate((
    TYPE_SIEGE,
    TYPE_SERVICE_CENTRAL,
    TYPE_BUREAU,
    TYPE_INSTITUT,
    TYPE_ANTENNE,
    TYPE_CNF,
    TYPE_CNFP,
    TYPE_CAI,)
))


def get_capitals_data(codes_pays):
    filename = os.path.join(os.path.dirname(__file__), 'static', 'data',
                            'country_capitals.json')
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        capitals_json = f.read()
    raw_capitals_data = json.loads(capitals_json)
    capitals_data = {}
    for capital_data in raw_capitals_data:
        try:
            country_code = capital_data['CountryCode']
            if country_code != u'NULL':
                code_iso3 = codes_pays[country_code]
                capitals_data[code_iso3] = {
                    'lon': float(capital_data['CapitalLongitude']),
                    'lat': float(capital_data['CapitalLatitude']),
                }
        except KeyError:
            pass
    return capitals_data


def get_countries_geojson():
    filename = os.path.join(os.path.dirname(__file__), 'static', 'data',
                            'countries.geojson')
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        countries_json = f.read()
    return json.loads(countries_json)


def sort_implantations(implantations_list):
    def implantation_key(implantation):
        return ORDRE_TYPES_IMPLANTATIONS[implantation.type], implantation.nom
    return sorted(implantations_list, key=implantation_key)


def make_implantation_data(implantations_list):
    return [{'id': implantation.id, 'nom': implantation.nom}
            for implantation in implantations_list]


def get_implantations_par_pays(implantations):
    """Construire un dictionnaire d'informations sur les implantations groupées
    par code pays.

    :param implantations: list[auf_refs.Implantation]
    :return: dict[str, dict]
    """
    liste_implantations = [i for i in implantations if i.type != TYPE_CNFP]
    grouped_implantations = itertools.groupby(
        liste_implantations, key=lambda imp: imp.adresse_postale_pays.code)
    implantations_par_pays = dict(
        (k, make_implantation_data(sort_implantations(g)))
        for k, g in grouped_implantations)
    return implantations_par_pays


def get_etablissements_par_pays_counter(etablissements):
    pays_etablissements = [e.pays for e in etablissements]
    return collections.Counter(pays_etablissements)


def get_lieux_implantations(coords_implantations):
    """

    :param coords_implantations: list[models.CoordonneesImplantations]
    :return: list[tuple]
    """
    lieux = {}
    for coord in coords_implantations:
        point = (coord.latitude, coord.longitude)
        implantation = coord.implantation
        try:
            lieu = lieux[point]
            implantations = lieu['implantations']
        except KeyError:
            implantations = []
            code_bureau = implantation.adresse_physique_pays.code_bureau_id
            lieu = {
                'lat': float(coord.latitude),
                'lon': float(coord.longitude),
                'nom': implantation.adresse_physique_ville,
                'code_bureau': code_bureau,
                'implantations': implantations}
            lieux[point] = lieu

        implantations.append({'nom': implantation.nom,
                              'id': implantation.id})

    return lieux.values()


def get_donnees_pays(etablissements, implantations, liste_pays):
    etablissements_counter = get_etablissements_par_pays_counter(etablissements)
    cnfp_counter = collections.Counter(
        [i.adresse_postale_pays
         for i in implantations if i.type == TYPE_CNFP])
    implantations_par_pays = get_implantations_par_pays(implantations)
    donnees_pays = {}
    for pays in liste_pays:
        implantations = implantations_par_pays.get(pays.code, [])
        nb_etablissements = etablissements_counter[pays]
        nb_cnfp = cnfp_counter[pays]
        donnees_pays[pays.code_iso3] = {
            'nom': pays.nom,
            'bureau': pays.code_bureau_id,
            'presence_auf': bool(implantations or nb_cnfp or nb_etablissements),
            'implantations': implantations,
            'nb_etablissements': nb_etablissements,
            'nb_cnfp': nb_cnfp,
        }
    return donnees_pays


def donnees_carte_json(request):
    implantations = auf_refs.Implantation.ouvertes\
        .only('nom', 'adresse_postale_pays', 'type')\
        .select_related('adresse_postale_pays')\
        .order_by('adresse_postale_pays__code')

    etablissements = auf_refs.Etablissement.objects\
        .only('nom', 'pays').select_related('pays')

    liste_pays = auf_refs.Pays.objects.all()
    donnees_pays = get_donnees_pays(etablissements, implantations, liste_pays)
    codes_pays = dict((pays.code, pays.code_iso3) for pays in liste_pays)
    all_coords = models.CoordonneesImplantations.objects\
        .select_related('implantation', 'implantation__adresse_physique_pays')\
        .all()
    lieux = get_lieux_implantations(
        all_coords)
    data = {
        'donnees_pays': donnees_pays,
        'capitales': get_capitals_data(codes_pays),
        'countries_geojson': get_countries_geojson(),
        'lieux_implantations': lieux,
    }
    return django.http.HttpResponse(json.dumps(data),
                                    mimetype='application/json')


def test_carte(request):
    return django.shortcuts.render(
        request, 'carte/test.html', {
            'bureaux': auf_refs.Bureau.objects.all()
        })