# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table(u'speakers_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'speakers', ['Speaker'])


    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table(u'speakers_speaker')


    models = {
        u'speakers.speaker': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Speaker'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['speakers']