# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('resume', models.TextField(null=True, blank=True)),
                ('texte', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'actualite', blank=True)),
                ('date_debut', models.DateField(null=True, blank=True)),
                ('date_fin', models.DateField(null=True, blank=True)),
                ('date_pub', models.DateField(verbose_name=b'date')),
                ('date_mod', models.DateTimeField(auto_now_add=True, verbose_name=b'date de derniere modification')),
                ('une', models.BooleanField(verbose_name=b'Garder cette actualit\xc3\xa9 en haut de liste')),
                ('status', models.CharField(default=b'3', max_length=1, choices=[(b'1', b'En cours de redaction'), (b'2', b'Propose a la publication'), (b'3', b'Publie en Ligne'), (b'4', b'A supprimer')])),
                ('bureau', models.ManyToManyField(to='references.Region')),
            ],
            options={
                'ordering': ('-date_pub',),
                'db_table': 'auf_site_institutionnel_actualite',
            },
            bases=(models.Model,),
        ),
    ]
