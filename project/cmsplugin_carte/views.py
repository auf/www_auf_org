# encoding: utf-8

import json

from auf.django.references.models import Pays, Region
from django.http import HttpResponse


LAT_LONG = {
    'A': (45.5, -73.55),
    'ACGL': (3.867, 11.517),
    'AO': (14.683, -17.433),
    'AP': (21.033, 105.85),
    'C': (18.533, -72.333),
    'ECO': (44.433, 26.1),
    'EO': (50.833, 4.35),
    'M': (34.033, -6.833),
    'MO': (33.883, 35.5),
    'OI': (-18.933, 47.517),
}

def pays_json(request):
    data = {}
    for pays in Pays.objects.all():
        data[pays.code_iso3] = {
            'id': pays.code_iso3,
            'name': pays.nom,
            'fillKey': 'B' + pays.region.code
        }
    return HttpResponse(json.dumps(data), mimetype='application/json')


def bureaux_json(request):
    regions = Region.objects.all()
    data = []
    for region in regions:
        if region.code in LAT_LONG:
            latitude, longitude = LAT_LONG[region.code]
            data.append({
                'latitude': latitude,
                'longitude': longitude,
                'radius': 4,
                'nom': 'Bureau ' + region.nom
            })
    return HttpResponse(json.dumps(data), mimetype='application/json')
