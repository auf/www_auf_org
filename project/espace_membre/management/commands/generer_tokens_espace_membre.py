# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from project.espace_membre import models as espace_membre


class Command(BaseCommand):
    help = u"Crée les token d'accès pour les établissemts qui n'en ont pas."

    def handle(self, *args, **options):
        etablissements = espace_membre.Etablissement.objects.all()
        tokens = set()
        for e in espace_membre.Acces.objects.filter(active__exact=1).all():
            tokens.add(e.id)

        for e in etablissements:
            if not e.id in tokens:
                new_t = espace_membre.Acces(etablissement=e)
                new_t.generer_token()
                new_t.active = True
                new_t.save()
