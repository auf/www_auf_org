# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Etablissement.nombre_etudiants'
        db.add_column(u'espace_membre_etablissement', 'nombre_etudiants',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Etablissement.nombre_chercheurs'
        db.add_column(u'espace_membre_etablissement', 'nombre_chercheurs',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Etablissement.nombre_enseignants'
        db.add_column(u'espace_membre_etablissement', 'nombre_enseignants',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Etablissement.nombre_membres'
        db.add_column(u'espace_membre_etablissement', 'nombre_membres',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Etablissement.responsable_courriel'
        db.add_column(u'espace_membre_etablissement', 'responsable_courriel',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)


        # Changing field 'Etablissement.url'
        db.alter_column(u'espace_membre_etablissement', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=255))

        # Changing field 'ResponsableModification.fonction'
        db.alter_column(u'espace_membre_responsablemodification', 'fonction', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Responsable.fonction'
        db.alter_column(u'espace_membre_responsable', 'fonction', self.gf('django.db.models.fields.CharField')(max_length=128))
        # Adding field 'EtablissementModification.nombre_etudiants'
        db.add_column(u'espace_membre_etablissementmodification', 'nombre_etudiants',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EtablissementModification.nombre_chercheurs'
        db.add_column(u'espace_membre_etablissementmodification', 'nombre_chercheurs',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EtablissementModification.nombre_enseignants'
        db.add_column(u'espace_membre_etablissementmodification', 'nombre_enseignants',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EtablissementModification.nombre_membres'
        db.add_column(u'espace_membre_etablissementmodification', 'nombre_membres',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EtablissementModification.responsable_courriel'
        db.add_column(u'espace_membre_etablissementmodification', 'responsable_courriel',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'EtablissementModification.export_gde_sai'
        db.add_column(u'espace_membre_etablissementmodification', 'export_gde_sai',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'EtablissementModification.export_gde_com'
        db.add_column(u'espace_membre_etablissementmodification', 'export_gde_com',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'EtablissementModification.url'
        db.alter_column(u'espace_membre_etablissementmodification', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=255))

    def backwards(self, orm):
        # Deleting field 'Etablissement.nombre_etudiants'
        db.delete_column(u'espace_membre_etablissement', 'nombre_etudiants')

        # Deleting field 'Etablissement.nombre_chercheurs'
        db.delete_column(u'espace_membre_etablissement', 'nombre_chercheurs')

        # Deleting field 'Etablissement.nombre_enseignants'
        db.delete_column(u'espace_membre_etablissement', 'nombre_enseignants')

        # Deleting field 'Etablissement.nombre_membres'
        db.delete_column(u'espace_membre_etablissement', 'nombre_membres')

        # Deleting field 'Etablissement.responsable_courriel'
        db.delete_column(u'espace_membre_etablissement', 'responsable_courriel')


        # Changing field 'Etablissement.url'
        db.alter_column(u'espace_membre_etablissement', 'url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

        # Changing field 'ResponsableModification.fonction'
        db.alter_column(u'espace_membre_responsablemodification', 'fonction', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'Responsable.fonction'
        db.alter_column(u'espace_membre_responsable', 'fonction', self.gf('django.db.models.fields.CharField')(max_length=64))
        # Deleting field 'EtablissementModification.nombre_etudiants'
        db.delete_column(u'espace_membre_etablissementmodification', 'nombre_etudiants')

        # Deleting field 'EtablissementModification.nombre_chercheurs'
        db.delete_column(u'espace_membre_etablissementmodification', 'nombre_chercheurs')

        # Deleting field 'EtablissementModification.nombre_enseignants'
        db.delete_column(u'espace_membre_etablissementmodification', 'nombre_enseignants')

        # Deleting field 'EtablissementModification.nombre_membres'
        db.delete_column(u'espace_membre_etablissementmodification', 'nombre_membres')

        # Deleting field 'EtablissementModification.responsable_courriel'
        db.delete_column(u'espace_membre_etablissementmodification', 'responsable_courriel')

        # Deleting field 'EtablissementModification.export_gde_sai'
        db.delete_column(u'espace_membre_etablissementmodification', 'export_gde_sai')

        # Deleting field 'EtablissementModification.export_gde_com'
        db.delete_column(u'espace_membre_etablissementmodification', 'export_gde_com')


        # Changing field 'EtablissementModification.url'
        db.alter_column(u'espace_membre_etablissementmodification', 'url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'espace_membre.acces': {
            'Meta': {'object_name': 'Acces'},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['espace_membre.Etablissement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'espace_membre.courriel': {
            'Meta': {'object_name': 'Courriel'},
            'contenu': ('django.db.models.fields.TextField', [], {}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sujet': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_creation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'espace_membre.courriellog': {
            'Meta': {'object_name': 'CourrielLog'},
            'adresse_courriel': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'courriel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['espace_membre.Courriel']"}),
            'envoye': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'envoye_le': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['espace_membre.Etablissement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'espace_membre.etablissement': {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'implantation'", 'to': u"orm['references.Implantation']"}),
            'membre': ('django.db.models.fields.BooleanField', [], {}),
            'membre_adhesion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'nombre_chercheurs': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_enseignants': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_etudiants': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_membres': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to_field': "'code'", 'db_column': "'pays'", 'to': u"orm['references.Pays']"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publication_electronique': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publication_papier': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'qualite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'espace_membre_etablissement'", 'unique': 'True', 'null': 'True', 'to': u"orm['references.Etablissement']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'region'", 'to': u"orm['references.Region']"}),
            'responsable_courriel': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'responsable_fonction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'responsable_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sigle': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'statut': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'espace_membre.etablissementmodification': {
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
            'etablissement': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'modification'", 'unique': 'True', 'null': 'True', 'to': u"orm['espace_membre.Etablissement']"}),
            'export_gde_com': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'export_gde_sai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'historique': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'implantation'", 'to': u"orm['references.Implantation']"}),
            'membre': ('django.db.models.fields.BooleanField', [], {}),
            'membre_adhesion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'nombre_chercheurs': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_enseignants': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_etudiants': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_membres': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to_field': "'code'", 'db_column': "'pays'", 'to': u"orm['references.Pays']"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publication_electronique': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publication_papier': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'qualite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'espace_membre_etablissementmodification'", 'unique': 'True', 'null': 'True', 'to': u"orm['references.Etablissement']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'region'", 'to': u"orm['references.Region']"}),
            'responsable_courriel': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'responsable_fonction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'responsable_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sigle': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'statut': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'validation_com': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'validation_etablissement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'validation_sai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'espace_membre.responsable': {
            'Meta': {'object_name': 'Responsable'},
            'courriel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['espace_membre.Etablissement']"}),
            'fonction': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modification_par': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'salutation': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'sousfonction': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'espace_membre.responsablemodification': {
            'Meta': {'object_name': 'ResponsableModification'},
            'courriel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['espace_membre.EtablissementModification']"}),
            'fonction': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modification_par': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'responsable': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['espace_membre.Responsable']", 'unique': 'True', 'null': 'True'}),
            'salutation': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'sousfonction': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'references.bureau': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Bureau', 'db_table': "u'ref_bureau'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.Implantation']", 'db_column': "'implantation'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.Region']", 'db_column': "'region'"})
        },
        u'references.etablissement': {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'implantation'", 'to': u"orm['references.Implantation']"}),
            'membre': ('django.db.models.fields.BooleanField', [], {}),
            'membre_adhesion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre_chercheurs': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_enseignants': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_etudiants': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_membres': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to_field': "'code'", 'db_column': "'pays'", 'to': u"orm['references.Pays']"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'qualite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'region'", 'to': u"orm['references.Region']"}),
            'responsable_courriel': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'responsable_fonction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'responsable_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sigle': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'statut': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'references.implantation': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Implantation', 'db_table': "u'ref_implantation'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adresse_physique_bureau': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_code_postal': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'adresse_physique_code_postal_avant_ville': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse_physique_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'adresse_physique_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impl_adresse_physique'", 'to_field': "'code'", 'db_column': "'adresse_physique_pays'", 'to': u"orm['references.Pays']"}),
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
            'adresse_postale_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impl_adresse_postale'", 'to_field': "'code'", 'db_column': "'adresse_postale_pays'", 'to': u"orm['references.Pays']"}),
            'adresse_postale_precision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_precision_avant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_rue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_ville': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bureau_rattachement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.Implantation']", 'null': 'True', 'db_column': "'bureau_rattachement'", 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modif_date': ('django.db.models.fields.DateField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.Region']", 'db_column': "'region'"}),
            'remarque': ('django.db.models.fields.TextField', [], {}),
            'responsable_implantation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'statut': ('django.db.models.fields.IntegerField', [], {}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telephone_interne': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'zone_administrative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.ZoneAdministrative']"})
        },
        u'references.pays': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Pays', 'db_table': "u'ref_pays'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'code_bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.Bureau']", 'to_field': "'code'", 'null': 'True', 'db_column': "'code_bureau'", 'blank': 'True'}),
            'code_iso3': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'developpement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monnaie': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nord_sud': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.Region']", 'db_column': "'region'"})
        },
        u'references.region': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Region', 'db_table': "u'ref_region'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation_bureau': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gere_region'", 'null': 'True', 'db_column': "'implantation_bureau'", 'to': u"orm['references.Implantation']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'references.zoneadministrative': {
            'Meta': {'ordering': "['nom']", 'object_name': 'ZoneAdministrative', 'db_table': "'ref_zoneadministrative'", 'managed': 'False'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['espace_membre']