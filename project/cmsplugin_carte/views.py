# encoding: utf-8

import json

from auf.django.references.models import Pays
from django.http import HttpResponse


def pays_json(request):
    data = {}
    for pays in Pays.objects.all():
        data[pays.code_iso3] = {
            'id': pays.code_iso3,
            'name': pays.nom,
            'fillKey': 'B' + pays.region.code
        }
    return HttpResponse(json.dumps(data), mimetype='application/json')
