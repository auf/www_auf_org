# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('layout_template', models.CharField(help_text=b'Utiliser le template pour afficher le contenu de la liste', max_length=256, verbose_name=b"Template utilis\xc3\xa9 pour l'affichage", choices=[(b'cmsplugin_pagelist/layouts/default.html', b'Default')])),
                ('nbelements', models.IntegerField(default=6, help_text=b"Le nombre d'\xc3\xa9l\xc3\xa9ments \xc3\xa0 afficher ?")),
                ('root', models.ForeignKey(default=1, to='cms.Page', help_text=b'Selectionnez la page racine dont vous voulez afficher le contenu (liste des sous pages)')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
