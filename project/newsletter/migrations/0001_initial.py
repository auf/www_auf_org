# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Newsletter'
        db.create_table('newsletter_newsletter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=11)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('titre_dossier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('texte_dossier', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('photo_dossier', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('lien_dossier', self.gf('django.db.models.fields.URLField')(max_length=300, null=True, blank=True)),
            ('lien', self.gf('django.db.models.fields.EmailField')(default='webmestre@auf.org', max_length=200)),
            ('lien2', self.gf('django.db.models.fields.URLField')(default='http://www.auf.org', max_length=250)),
            ('lienFace', self.gf('django.db.models.fields.URLField')(default='http://www.facebook.com/aufinternational', max_length=250)),
            ('abonne', self.gf('django.db.models.fields.IntegerField')(default='1000', max_length=11)),
            ('footer', self.gf('django.db.models.fields.TextField')(default='Lettre electronique est une publication realisee par Agence universitaire de la Francophonie. AUF operateur direct de la Francophonie est un reseau mondial de 781 etablissements enseignement superieur et de recherche.')),
        ))
        db.send_create_signal('newsletter', ['Newsletter'])

        # Adding M2M table for field bureau on 'Newsletter'
        db.create_table('newsletter_newsletter_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm['newsletter.newsletter'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('newsletter_newsletter_bureau', ['newsletter_id', 'region_id'])

        # Adding M2M table for field appel on 'Newsletter'
        db.create_table('newsletter_newsletter_appel', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm['newsletter.newsletter'], null=False)),
            ('appel_offre', models.ForeignKey(orm['auf_site_institutionnel.appel_offre'], null=False))
        ))
        db.create_unique('newsletter_newsletter_appel', ['newsletter_id', 'appel_offre_id'])

        # Adding M2M table for field actualite on 'Newsletter'
        db.create_table('newsletter_newsletter_actualite', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm['newsletter.newsletter'], null=False)),
            ('actualite', models.ForeignKey(orm['auf_site_institutionnel.actualite'], null=False))
        ))
        db.create_unique('newsletter_newsletter_actualite', ['newsletter_id', 'actualite_id'])

        # Adding M2M table for field evenement on 'Newsletter'
        db.create_table('newsletter_newsletter_evenement', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm['newsletter.newsletter'], null=False)),
            ('evenement', models.ForeignKey(orm['auf_site_institutionnel.evenement'], null=False))
        ))
        db.create_unique('newsletter_newsletter_evenement', ['newsletter_id', 'evenement_id'])

        # Adding M2M table for field publication on 'Newsletter'
        db.create_table('newsletter_newsletter_publication', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm['newsletter.newsletter'], null=False)),
            ('publication', models.ForeignKey(orm['auf_site_institutionnel.publication'], null=False))
        ))
        db.create_unique('newsletter_newsletter_publication', ['newsletter_id', 'publication_id'])

        # Adding model 'Abonne'
        db.create_table('newsletter_abonne', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('adresse', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('valide', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('newsletter', ['Abonne'])

        # Adding M2M table for field bureau on 'Abonne'
        db.create_table('newsletter_abonne_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('abonne', models.ForeignKey(orm['newsletter.abonne'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('newsletter_abonne_bureau', ['abonne_id', 'region_id'])

        # Adding model 'Fil'
        db.create_table('newsletter_fil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=11)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('footer', self.gf('django.db.models.fields.TextField')(default='Copyright AUF 2013')),
        ))
        db.send_create_signal('newsletter', ['Fil'])

        # Adding M2M table for field bureau on 'Fil'
        db.create_table('newsletter_fil_bureau', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fil', models.ForeignKey(orm['newsletter.fil'], null=False)),
            ('region', models.ForeignKey(orm['site_references.region'], null=False))
        ))
        db.create_unique('newsletter_fil_bureau', ['fil_id', 'region_id'])

        # Adding M2M table for field actualite on 'Fil'
        db.create_table('newsletter_fil_actualite', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fil', models.ForeignKey(orm['newsletter.fil'], null=False)),
            ('actualite', models.ForeignKey(orm['auf_site_institutionnel.actualite'], null=False))
        ))
        db.create_unique('newsletter_fil_actualite', ['fil_id', 'actualite_id'])

        # Adding M2M table for field evenement on 'Fil'
        db.create_table('newsletter_fil_evenement', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fil', models.ForeignKey(orm['newsletter.fil'], null=False)),
            ('evenement', models.ForeignKey(orm['auf_site_institutionnel.evenement'], null=False))
        ))
        db.create_unique('newsletter_fil_evenement', ['fil_id', 'evenement_id'])

        # Adding model 'Planete'
        db.create_table('newsletter_planete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=11)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('titre_dossier', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('texte_dossier', self.gf('django.db.models.fields.TextField')()),
            ('photo_dossier', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('lien_dossier', self.gf('django.db.models.fields.URLField')(max_length=300, null=True, blank=True)),
            ('fil_planete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['newsletter.Fil'])),
            ('footer', self.gf('django.db.models.fields.TextField')(default='Lettre electronique est une publication realisee par Agence universitaire de la Francophonie. AUF operateur direct de la Francophonie est un reseau mondial de 781 etablissements enseignement superieur et de recherche.')),
        ))
        db.send_create_signal('newsletter', ['Planete'])

        # Adding M2M table for field appel_planete on 'Planete'
        db.create_table('newsletter_planete_appel_planete', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('planete', models.ForeignKey(orm['newsletter.planete'], null=False)),
            ('appel_offre', models.ForeignKey(orm['auf_site_institutionnel.appel_offre'], null=False))
        ))
        db.create_unique('newsletter_planete_appel_planete', ['planete_id', 'appel_offre_id'])

        # Adding M2M table for field bourse_planete on 'Planete'
        db.create_table('newsletter_planete_bourse_planete', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('planete', models.ForeignKey(orm['newsletter.planete'], null=False)),
            ('bourse', models.ForeignKey(orm['auf_site_institutionnel.bourse'], null=False))
        ))
        db.create_unique('newsletter_planete_bourse_planete', ['planete_id', 'bourse_id'])

        # Adding M2M table for field evenement_planete on 'Planete'
        db.create_table('newsletter_planete_evenement_planete', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('planete', models.ForeignKey(orm['newsletter.planete'], null=False)),
            ('evenement', models.ForeignKey(orm['auf_site_institutionnel.evenement'], null=False))
        ))
        db.create_unique('newsletter_planete_evenement_planete', ['planete_id', 'evenement_id'])

        # Adding model 'ProjetPlanete'
        db.create_table('newsletter_projetplanete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('planete', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projets', to=orm['newsletter.Planete'])),
            ('titre_projet', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('texte_projet', self.gf('django.db.models.fields.TextField')()),
            ('photo_projet', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('lien_projet', self.gf('django.db.models.fields.URLField')(max_length=300)),
            ('ordre_projet', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('newsletter', ['ProjetPlanete'])

        # Adding model 'MembrePlanete'
        db.create_table('newsletter_membreplanete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('planete', self.gf('django.db.models.fields.related.ForeignKey')(related_name='membres', to=orm['newsletter.Planete'])),
            ('titre_membre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('texte_membre', self.gf('django.db.models.fields.TextField')()),
            ('photo_membre', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('lien_membre', self.gf('django.db.models.fields.URLField')(max_length=300)),
            ('ordre_membre', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('newsletter', ['MembrePlanete'])

        # Adding model 'Breve'
        db.create_table('newsletter_breve', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=11)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('texte_intro', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('texte_rh', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('texte_ari', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('texte_agenda', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('texte_mission', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('texte_arrive', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('texte_diver', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('texte_autre', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('footer', self.gf('django.db.models.fields.TextField')(default="Les br\xc3\xa8ves des services centraux sont une publication r\xc3\xa9alis\xc3\xa9e par l'Agence universitaire de la Francophonie. L'AUF, op\xc3\xa9rateur de la Francophonie, est un r\xc3\xa9seau mondial de 800 \xc3\xa9tablissements d'enseignement sup\xc3\xa9rieur et de recherche.")),
        ))
        db.send_create_signal('newsletter', ['Breve'])

        # Adding model 'VideoPlugin'
        db.create_table('cmsplugin_videoplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('video', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('newsletter', ['VideoPlugin'])


    def backwards(self, orm):
        # Deleting model 'Newsletter'
        db.delete_table('newsletter_newsletter')

        # Removing M2M table for field bureau on 'Newsletter'
        db.delete_table('newsletter_newsletter_bureau')

        # Removing M2M table for field appel on 'Newsletter'
        db.delete_table('newsletter_newsletter_appel')

        # Removing M2M table for field actualite on 'Newsletter'
        db.delete_table('newsletter_newsletter_actualite')

        # Removing M2M table for field evenement on 'Newsletter'
        db.delete_table('newsletter_newsletter_evenement')

        # Removing M2M table for field publication on 'Newsletter'
        db.delete_table('newsletter_newsletter_publication')

        # Deleting model 'Abonne'
        db.delete_table('newsletter_abonne')

        # Removing M2M table for field bureau on 'Abonne'
        db.delete_table('newsletter_abonne_bureau')

        # Deleting model 'Fil'
        db.delete_table('newsletter_fil')

        # Removing M2M table for field bureau on 'Fil'
        db.delete_table('newsletter_fil_bureau')

        # Removing M2M table for field actualite on 'Fil'
        db.delete_table('newsletter_fil_actualite')

        # Removing M2M table for field evenement on 'Fil'
        db.delete_table('newsletter_fil_evenement')

        # Deleting model 'Planete'
        db.delete_table('newsletter_planete')

        # Removing M2M table for field appel_planete on 'Planete'
        db.delete_table('newsletter_planete_appel_planete')

        # Removing M2M table for field bourse_planete on 'Planete'
        db.delete_table('newsletter_planete_bourse_planete')

        # Removing M2M table for field evenement_planete on 'Planete'
        db.delete_table('newsletter_planete_evenement_planete')

        # Deleting model 'ProjetPlanete'
        db.delete_table('newsletter_projetplanete')

        # Deleting model 'MembrePlanete'
        db.delete_table('newsletter_membreplanete')

        # Deleting model 'Breve'
        db.delete_table('newsletter_breve')

        # Deleting model 'VideoPlugin'
        db.delete_table('cmsplugin_videoplugin')


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
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 11, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'newsletter.abonne': {
            'Meta': {'object_name': 'Abonne'},
            'adresse': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valide': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'newsletter.breve': {
            'Meta': {'object_name': 'Breve'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'footer': ('django.db.models.fields.TextField', [], {'default': '"Les br\\xc3\\xa8ves des services centraux sont une publication r\\xc3\\xa9alis\\xc3\\xa9e par l\'Agence universitaire de la Francophonie. L\'AUF, op\\xc3\\xa9rateur de la Francophonie, est un r\\xc3\\xa9seau mondial de 800 \\xc3\\xa9tablissements d\'enseignement sup\\xc3\\xa9rieur et de recherche."'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '11'}),
            'texte_agenda': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'texte_ari': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'texte_arrive': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'texte_autre': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'texte_diver': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'texte_intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'texte_mission': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'texte_rh': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'newsletter.fil': {
            'Meta': {'object_name': 'Fil'},
            'actualite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Actualite']", 'null': 'True', 'blank': 'True'}),
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'evenement': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Evenement']", 'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.TextField', [], {'default': "'Copyright AUF 2013'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '11'})
        },
        'newsletter.membreplanete': {
            'Meta': {'object_name': 'MembrePlanete'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien_membre': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'ordre_membre': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'photo_membre': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'planete': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'membres'", 'to': "orm['newsletter.Planete']"}),
            'texte_membre': ('django.db.models.fields.TextField', [], {}),
            'titre_membre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'newsletter.newsletter': {
            'Meta': {'object_name': 'Newsletter'},
            'abonne': ('django.db.models.fields.IntegerField', [], {'default': "'1000'", 'max_length': '11'}),
            'actualite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Actualite']", 'null': 'True', 'blank': 'True'}),
            'appel': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Appel_Offre']"}),
            'bureau': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['site_references.Region']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'evenement': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Evenement']", 'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.TextField', [], {'default': "'Lettre electronique est une publication realisee par Agence universitaire de la Francophonie. AUF operateur direct de la Francophonie est un reseau mondial de 781 etablissements enseignement superieur et de recherche.'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien': ('django.db.models.fields.EmailField', [], {'default': "'webmestre@auf.org'", 'max_length': '200'}),
            'lien2': ('django.db.models.fields.URLField', [], {'default': "'http://www.auf.org'", 'max_length': '250'}),
            'lienFace': ('django.db.models.fields.URLField', [], {'default': "'http://www.facebook.com/aufinternational'", 'max_length': '250'}),
            'lien_dossier': ('django.db.models.fields.URLField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '11'}),
            'photo_dossier': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publication': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Publication']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte_dossier': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titre_dossier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'newsletter.planete': {
            'Meta': {'object_name': 'Planete'},
            'appel_planete': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Appel_Offre']", 'null': 'True', 'blank': 'True'}),
            'bourse_planete': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Bourse']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'evenement_planete': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auf_site_institutionnel.Evenement']", 'null': 'True', 'blank': 'True'}),
            'fil_planete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['newsletter.Fil']"}),
            'footer': ('django.db.models.fields.TextField', [], {'default': "'Lettre electronique est une publication realisee par Agence universitaire de la Francophonie. AUF operateur direct de la Francophonie est un reseau mondial de 781 etablissements enseignement superieur et de recherche.'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien_dossier': ('django.db.models.fields.URLField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '11'}),
            'photo_dossier': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'texte_dossier': ('django.db.models.fields.TextField', [], {}),
            'titre_dossier': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'newsletter.projetplanete': {
            'Meta': {'object_name': 'ProjetPlanete'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien_projet': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'ordre_projet': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'photo_projet': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'planete': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projets'", 'to': "orm['newsletter.Planete']"}),
            'texte_projet': ('django.db.models.fields.TextField', [], {}),
            'titre_projet': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'newsletter.videoplugin': {
            'Meta': {'object_name': 'VideoPlugin', 'db_table': "'cmsplugin_videoplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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

    complete_apps = ['newsletter']