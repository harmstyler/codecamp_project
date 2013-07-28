# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Session'
        db.create_table(u'campsessions_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'campsessions', ['Session'])

        # Adding M2M table for field speakers on 'Session'
        m2m_table_name = db.shorten_name(u'campsessions_session_speakers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('session', models.ForeignKey(orm[u'campsessions.session'], null=False)),
            ('speaker', models.ForeignKey(orm[u'speakers.speaker'], null=False))
        ))
        db.create_unique(m2m_table_name, ['session_id', 'speaker_id'])


    def backwards(self, orm):
        # Deleting model 'Session'
        db.delete_table(u'campsessions_session')

        # Removing M2M table for field speakers on 'Session'
        db.delete_table(db.shorten_name(u'campsessions_session_speakers'))


    models = {
        u'campsessions.session': {
            'Meta': {'ordering': "['title']", 'object_name': 'Session'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['speakers.Speaker']", 'symmetrical': 'False'}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
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

    complete_apps = ['campsessions']