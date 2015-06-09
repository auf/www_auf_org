# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Etablissement'
        db.create_table('espace_membre_etablissement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sigle', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('pays', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to_field='code', db_column='pays', to=orm['references.Pays'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, db_column='region', to=orm['references.Region'])),
            ('implantation', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, db_column='implantation', to=orm['references.Implantation'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('historique', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('membre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('membre_adhesion_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('statut', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('qualite', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('responsable_genre', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('responsable_nom', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('responsable_prenom', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('responsable_fonction', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('code_postal', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cedex', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('commentaire', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ref', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='espace_membre_etablissement', unique=True, null=True, to=orm['references.Etablissement'])),
            ('courriel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('nombre', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('chiffres_cles', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('publication_papier', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('publication_electronique', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('espace_membre', ['Etablissement'])

        # Adding model 'EtablissementModification'
        db.create_table('espace_membre_etablissementmodification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sigle', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('pays', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to_field='code', db_column='pays', to=orm['references.Pays'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, db_column='region', to=orm['references.Region'])),
            ('implantation', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, db_column='implantation', to=orm['references.Implantation'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('historique', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('membre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('membre_adhesion_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('statut', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('qualite', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('responsable_genre', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('responsable_nom', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('responsable_prenom', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('responsable_fonction', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('code_postal', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cedex', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('commentaire', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ref', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='espace_membre_etablissementmodification', unique=True, null=True, to=orm['references.Etablissement'])),
            ('courriel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('nombre', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('chiffres_cles', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('publication_papier', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('publication_electronique', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('etablissement', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['espace_membre.Etablissement'], unique=True, null=True)),
            ('validation_etablissement', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('validation_sai', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('validation_com', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_validation_etablissement', self.gf('django.db.models.fields.DateField')(null=True)),
            ('date_validation_sai', self.gf('django.db.models.fields.DateField')(null=True)),
            ('date_validation_com', self.gf('django.db.models.fields.DateField')(null=True)),
            ('a_valider_sai', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('a_valider_com', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('espace_membre', ['EtablissementModification'])

        # Adding model 'Responsable'
        db.create_table('espace_membre_responsable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('courriel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modification_par', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('etablissement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['espace_membre.Etablissement'])),
        ))
        db.send_create_signal('espace_membre', ['Responsable'])

        # Adding model 'ResponsableModification'
        db.create_table('espace_membre_responsablemodification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('courriel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('modification_par', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('etablissement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['espace_membre.EtablissementModification'])),
            ('responsable', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['espace_membre.Responsable'], unique=True, null=True)),
        ))
        db.send_create_signal('espace_membre', ['ResponsableModification'])

        # Adding model 'Acces'
        db.create_table('espace_membre_acces', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('etablissement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['espace_membre.Etablissement'])),
            ('token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('espace_membre', ['Acces'])

        # Adding model 'Courriel'
        db.create_table('espace_membre_courriel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user_creation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sujet', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contenu', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('espace_membre', ['Courriel'])

        # Adding model 'CourrielLog'
        db.create_table('espace_membre_courriellog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('courriel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['espace_membre.Courriel'])),
            ('etablissement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['espace_membre.Etablissement'])),
            ('adresse_courriel', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('envoye', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('envoye_le', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('espace_membre', ['CourrielLog'])


    def backwards(self, orm):
        # Deleting model 'Etablissement'
        db.delete_table('espace_membre_etablissement')

        # Deleting model 'EtablissementModification'
        db.delete_table('espace_membre_etablissementmodification')

        # Deleting model 'Responsable'
        db.delete_table('espace_membre_responsable')

        # Deleting model 'ResponsableModification'
        db.delete_table('espace_membre_responsablemodification')

        # Deleting model 'Acces'
        db.delete_table('espace_membre_acces')

        # Deleting model 'Courriel'
        db.delete_table('espace_membre_courriel')

        # Deleting model 'CourrielLog'
        db.delete_table('espace_membre_courriellog')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'espace_membre.acces': {
            'Meta': {'object_name': 'Acces'},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['espace_membre.Etablissement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'espace_membre.courriel': {
            'Meta': {'object_name': 'Courriel'},
            'contenu': ('django.db.models.fields.TextField', [], {}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sujet': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_creation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'espace_membre.courriellog': {
            'Meta': {'object_name': 'CourrielLog'},
            'adresse_courriel': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'courriel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['espace_membre.Courriel']"}),
            'envoye': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'envoye_le': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['espace_membre.Etablissement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'espace_membre.etablissement': {
            'Meta': {'object_name': 'Etablissement'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cedex': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'chiffres_cles': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'commentaire': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'courriel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'date_modification': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'historique': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'implantation'", 'to': "orm['references.Implantation']"}),
            'membre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'membre_adhesion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to_field': "'code'", 'db_column': "'pays'", 'to': "orm['references.Pays']"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publication_electronique': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publication_papier': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'qualite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'espace_membre_etablissement'", 'unique': 'True', 'null': 'True', 'to': "orm['references.Etablissement']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'region'", 'to': "orm['references.Region']"}),
            'responsable_fonction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'responsable_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sigle': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'statut': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'espace_membre.etablissementmodification': {
            'Meta': {'object_name': 'EtablissementModification'},
            'a_valider_com': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'a_valider_sai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cedex': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'chiffres_cles': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'commentaire': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'courriel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'date_modification': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_validation_com': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_validation_etablissement': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_validation_sai': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'etablissement': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['espace_membre.Etablissement']", 'unique': 'True', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'historique': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'implantation'", 'to': "orm['references.Implantation']"}),
            'membre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'membre_adhesion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to_field': "'code'", 'db_column': "'pays'", 'to': "orm['references.Pays']"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publication_electronique': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publication_papier': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'qualite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'espace_membre_etablissementmodification'", 'unique': 'True', 'null': 'True', 'to': "orm['references.Etablissement']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'region'", 'to': "orm['references.Region']"}),
            'responsable_fonction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'responsable_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sigle': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'statut': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'validation_com': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'validation_etablissement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'validation_sai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'espace_membre.responsable': {
            'Meta': {'object_name': 'Responsable'},
            'courriel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['espace_membre.Etablissement']"}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modification_par': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'espace_membre.responsablemodification': {
            'Meta': {'object_name': 'ResponsableModification'},
            'courriel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['espace_membre.EtablissementModification']"}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modification_par': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'responsable': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['espace_membre.Responsable']", 'unique': 'True', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
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
        'references.etablissement': {
            'Meta': {'ordering': "['pays__nom', 'nom']", 'object_name': 'Etablissement', 'db_table': "u'ref_etablissement'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cedex': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'commentaire': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'historique': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'implantation'", 'to': "orm['references.Implantation']"}),
            'membre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'membre_adhesion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to_field': "'code'", 'db_column': "'pays'", 'to': "orm['references.Pays']"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'qualite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'region'", 'to': "orm['references.Region']"}),
            'responsable_fonction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'responsable_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sigle': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'statut': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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
        }
    }

    complete_apps = ['espace_membre']