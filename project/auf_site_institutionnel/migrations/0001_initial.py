# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Personna'
        db.create_table('auf_site_institutionnel_personna', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Personna'])

        # Adding model 'Bourse'
        db.create_table('auf_site_institutionnel_bourse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('resume', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date_fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_fin2', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Bourse'])

        # Adding M2M table for field bureau on 'Bourse'
        db.create_table('auf_site_institutionnel_bourse_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bourse', models.ForeignKey(orm['auf_site_institutionnel.bourse'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_bourse_bureau', ['bourse_id', 'region_id'])

        # Adding M2M table for field personna on 'Bourse'
        db.create_table('auf_site_institutionnel_bourse_personna', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bourse', models.ForeignKey(orm['auf_site_institutionnel.bourse'], null=False)),
            ('personna', models.ForeignKey(orm['auf_site_institutionnel.personna'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_bourse_personna', ['bourse_id', 'personna_id'])

        # Adding model 'Actualite'
        db.create_table('auf_site_institutionnel_actualite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('resume', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date_debut', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateField')()),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('une', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Actualite'])

        # Adding M2M table for field bureau on 'Actualite'
        db.create_table('auf_site_institutionnel_actualite_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actualite', models.ForeignKey(orm['auf_site_institutionnel.actualite'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_actualite_bureau', ['actualite_id', 'region_id'])

        # Adding M2M table for field personna on 'Actualite'
        db.create_table('auf_site_institutionnel_actualite_personna', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actualite', models.ForeignKey(orm['auf_site_institutionnel.actualite'], null=False)),
            ('personna', models.ForeignKey(orm['auf_site_institutionnel.personna'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_actualite_personna', ['actualite_id', 'personna_id'])

        # Adding model 'Veille'
        db.create_table('auf_site_institutionnel_veille', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('resume', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date_debut', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateField')()),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Veille'])

        # Adding M2M table for field bureau on 'Veille'
        db.create_table('auf_site_institutionnel_veille_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('veille', models.ForeignKey(orm['auf_site_institutionnel.veille'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_veille_bureau', ['veille_id', 'region_id'])

        # Adding M2M table for field personna on 'Veille'
        db.create_table('auf_site_institutionnel_veille_personna', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('veille', models.ForeignKey(orm['auf_site_institutionnel.veille'], null=False)),
            ('personna', models.ForeignKey(orm['auf_site_institutionnel.personna'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_veille_personna', ['veille_id', 'personna_id'])

        # Adding model 'Appel_Offre'
        db.create_table('auf_site_institutionnel_appel_offre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('auf', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('resume', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date_fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_fin2', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Appel_Offre'])

        # Adding M2M table for field bureau on 'Appel_Offre'
        db.create_table('auf_site_institutionnel_appel_offre_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appel_offre', models.ForeignKey(orm['auf_site_institutionnel.appel_offre'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_appel_offre_bureau', ['appel_offre_id', 'region_id'])

        # Adding M2M table for field personna on 'Appel_Offre'
        db.create_table('auf_site_institutionnel_appel_offre_personna', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appel_offre', models.ForeignKey(orm['auf_site_institutionnel.appel_offre'], null=False)),
            ('personna', models.ForeignKey(orm['auf_site_institutionnel.personna'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_appel_offre_personna', ['appel_offre_id', 'personna_id'])

        # Adding model 'Evenement'
        db.create_table('auf_site_institutionnel_evenement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('resume', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('lieu', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('detail_horaire', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_debut', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Evenement'])

        # Adding M2M table for field bureau on 'Evenement'
        db.create_table('auf_site_institutionnel_evenement_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('evenement', models.ForeignKey(orm['auf_site_institutionnel.evenement'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_evenement_bureau', ['evenement_id', 'region_id'])

        # Adding model 'Comares'
        db.create_table('auf_site_institutionnel_comares', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('resume', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateField')()),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Comares'])

        # Adding M2M table for field bureau on 'Comares'
        db.create_table('auf_site_institutionnel_comares_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comares', models.ForeignKey(orm['auf_site_institutionnel.comares'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_comares_bureau', ['comares_id', 'region_id'])

        # Adding model 'Publication'
        db.create_table('auf_site_institutionnel_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('resume', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')()),
            ('docu', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateField')()),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Publication'])

        # Adding M2M table for field bureau on 'Publication'
        db.create_table('auf_site_institutionnel_publication_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publication', models.ForeignKey(orm['auf_site_institutionnel.publication'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('auf_site_institutionnel_publication_bureau', ['publication_id', 'region_id'])

        # Adding model 'Partenaire'
        db.create_table('auf_site_institutionnel_partenaire', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('nom', self.gf('django.db.models.fields.TextField')()),
            ('objet', self.gf('django.db.models.fields.TextField')()),
            ('budget', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('periode', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('date_pub', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('auf_site_institutionnel', ['Partenaire'])


    def backwards(self, orm):
        # Deleting model 'Personna'
        db.delete_table('auf_site_institutionnel_personna')

        # Deleting model 'Bourse'
        db.delete_table('auf_site_institutionnel_bourse')

        # Removing M2M table for field bureau on 'Bourse'
        db.delete_table('auf_site_institutionnel_bourse_bureau')

        # Removing M2M table for field personna on 'Bourse'
        db.delete_table('auf_site_institutionnel_bourse_personna')

        # Deleting model 'Actualite'
        db.delete_table('auf_site_institutionnel_actualite')

        # Removing M2M table for field bureau on 'Actualite'
        db.delete_table('auf_site_institutionnel_actualite_bureau')

        # Removing M2M table for field personna on 'Actualite'
        db.delete_table('auf_site_institutionnel_actualite_personna')

        # Deleting model 'Veille'
        db.delete_table('auf_site_institutionnel_veille')

        # Removing M2M table for field bureau on 'Veille'
        db.delete_table('auf_site_institutionnel_veille_bureau')

        # Removing M2M table for field personna on 'Veille'
        db.delete_table('auf_site_institutionnel_veille_personna')

        # Deleting model 'Appel_Offre'
        db.delete_table('auf_site_institutionnel_appel_offre')

        # Removing M2M table for field bureau on 'Appel_Offre'
        db.delete_table('auf_site_institutionnel_appel_offre_bureau')

        # Removing M2M table for field personna on 'Appel_Offre'
        db.delete_table('auf_site_institutionnel_appel_offre_personna')

        # Deleting model 'Evenement'
        db.delete_table('auf_site_institutionnel_evenement')

        # Removing M2M table for field bureau on 'Evenement'
        db.delete_table('auf_site_institutionnel_evenement_bureau')

        # Deleting model 'Comares'
        db.delete_table('auf_site_institutionnel_comares')

        # Removing M2M table for field bureau on 'Comares'
        db.delete_table('auf_site_institutionnel_comares_bureau')

        # Deleting model 'Publication'
        db.delete_table('auf_site_institutionnel_publication')

        # Removing M2M table for field bureau on 'Publication'
        db.delete_table('auf_site_institutionnel_publication_bureau')

        # Deleting model 'Partenaire'
        db.delete_table('auf_site_institutionnel_partenaire')


    models = {
        'auf_site_institutionnel.actualite': {
            'Meta': {'ordering': "('-date_pub',)", 'object_name': 'Actualite'},
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date_debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'personna': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auf_site_institutionnel.Personna']", 'symmetrical': 'False'}),
            'resume': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte': ('django.db.models.fields.TextField', [], {}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'une': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'auf_site_institutionnel.appel_offre': {
            'Meta': {'ordering': "('-date_pub',)", 'object_name': 'Appel_Offre'},
            'auf': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fin2': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'personna': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auf_site_institutionnel.Personna']", 'symmetrical': 'False'}),
            'resume': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte': ('django.db.models.fields.TextField', [], {}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'auf_site_institutionnel.bourse': {
            'Meta': {'ordering': "('-date_pub',)", 'object_name': 'Bourse'},
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fin2': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'personna': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auf_site_institutionnel.Personna']", 'symmetrical': 'False'}),
            'resume': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte': ('django.db.models.fields.TextField', [], {}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'auf_site_institutionnel.comares': {
            'Meta': {'ordering': "('-date_pub',)", 'object_name': 'Comares'},
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte': ('django.db.models.fields.TextField', [], {}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'auf_site_institutionnel.evenement': {
            'Meta': {'ordering': "('-date_debut',)", 'object_name': 'Evenement'},
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date_debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'detail_horaire': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte': ('django.db.models.fields.TextField', [], {}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'auf_site_institutionnel.partenaire': {
            'Meta': {'object_name': 'Partenaire'},
            'budget': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {}),
            'objet': ('django.db.models.fields.TextField', [], {}),
            'periode': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'auf_site_institutionnel.personna': {
            'Meta': {'object_name': 'Personna'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'auf_site_institutionnel.publication': {
            'Meta': {'ordering': "('-date_pub',)", 'object_name': 'Publication'},
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateField', [], {}),
            'docu': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte': ('django.db.models.fields.TextField', [], {}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'auf_site_institutionnel.veille': {
            'Meta': {'ordering': "('-date_pub',)", 'object_name': 'Veille'},
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date_debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pub': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'personna': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auf_site_institutionnel.Personna']", 'symmetrical': 'False'}),
            'resume': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte': ('django.db.models.fields.TextField', [], {}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'references.bureau': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Bureau', 'db_table': "u'ref_bureau'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Implantation']", 'db_column': "'implantation'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Region']", 'db_column': "'region'"})
        },
        'references.implantation': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Implantation', 'db_table': "u'ref_implantation'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adresse_physique_bureau': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_code_postal': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'adresse_physique_code_postal_avant_ville': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse_physique_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'adresse_physique_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impl_adresse_physique'", 'to_field': "'code'", 'db_column': "'adresse_physique_pays'", 'to': "orm['references.Pays']"}),
            'adresse_physique_precision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_precision_avant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_rue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_ville': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'adresse_postale_boite_postale': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_bureau': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_code_postal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_code_postal_avant_ville': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse_postale_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impl_adresse_postale'", 'to_field': "'code'", 'db_column': "'adresse_postale_pays'", 'to': "orm['references.Pays']"}),
            'adresse_postale_precision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_precision_avant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_rue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_ville': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bureau_rattachement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Implantation']", 'db_column': "'bureau_rattachement'"}),
            'code_meteo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'commentaire': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'courriel': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'courriel_interne': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'date_extension': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fermeture': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_inauguration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_ouverture': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fax_interne': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fuseau_horaire': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hebergement_convention': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'hebergement_convention_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hebergement_etablissement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modif_date': ('django.db.models.fields.DateField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Region']", 'db_column': "'region'"}),
            'remarque': ('django.db.models.fields.TextField', [], {}),
            'responsable_implantation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'statut': ('django.db.models.fields.IntegerField', [], {}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telephone_interne': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        'references.pays': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Pays', 'db_table': "u'ref_pays'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'code_bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Bureau']", 'to_field': "'code'", 'null': 'True', 'db_column': "'code_bureau'", 'blank': 'True'}),
            'code_iso3': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'developpement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monnaie': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nord_sud': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['references.Region']", 'db_column': "'region'"})
        },
        'references.region': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Region', 'db_table': "u'ref_region'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation_bureau': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gere_region'", 'null': 'True', 'db_column': "'implantation_bureau'", 'to': "orm['references.Implantation']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'site_references.region': {
            'Meta': {'object_name': 'Region', 'db_table': "'ref_region'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'implantation_bureau': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'db_column': "'implantation_bureau'", 'to': "orm['references.Implantation']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['auf_site_institutionnel']