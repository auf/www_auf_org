# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carousel'
        db.create_table(u'cmsplugin_bootstrap_carousel_carousel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('domid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('interval', self.gf('django.db.models.fields.IntegerField')(default=5000)),
            ('show_title', self.gf('django.db.models.fields.BooleanField')()),
            ('show_caption', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'cmsplugin_bootstrap_carousel', ['Carousel'])

        # Adding model 'CarouselItem'
        db.create_table(u'cmsplugin_bootstrap_carousel_carouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carousel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_bootstrap_carousel.Carousel'])),
            ('caption_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('caption_content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(default=None, max_length=256, blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_bootstrap_carousel', ['CarouselItem'])


    def backwards(self, orm):
        # Deleting model 'Carousel'
        db.delete_table(u'cmsplugin_bootstrap_carousel_carousel')

        # Deleting model 'CarouselItem'
        db.delete_table(u'cmsplugin_bootstrap_carousel_carouselitem')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_bootstrap_carousel.carousel': {
            'Meta': {'object_name': 'Carousel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'domid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'show_caption': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'cmsplugin_bootstrap_carousel.carouselitem': {
            'Meta': {'object_name': 'CarouselItem'},
            'caption_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caption_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsplugin_bootstrap_carousel.Carousel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_bootstrap_carousel']