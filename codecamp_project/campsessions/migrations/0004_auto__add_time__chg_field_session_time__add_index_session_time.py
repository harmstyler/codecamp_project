# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Time'
        db.create_table(u'campsessions_time', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'campsessions', ['Time'])


        # Renaming column for 'Session.time' to match new field type.
        db.rename_column(u'campsessions_session', 'time', 'time_id')
        # Changing field 'Session.time'
        db.alter_column(u'campsessions_session', 'time_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campsessions.Time'], null=True))
        # Adding index on 'Session', fields ['time']
        db.create_index(u'campsessions_session', ['time_id'])


    def backwards(self, orm):
        # Removing index on 'Session', fields ['time']
        db.delete_index(u'campsessions_session', ['time_id'])

        # Deleting model 'Time'
        db.delete_table(u'campsessions_time')


        # Renaming column for 'Session.time' to match new field type.
        db.rename_column(u'campsessions_session', 'time_id', 'time')
        # Changing field 'Session.time'
        db.alter_column(u'campsessions_session', 'time', self.gf('django.db.models.fields.TimeField')(default=0))

    models = {
        u'campsessions.room': {
            'Meta': {'ordering': "['name']", 'object_name': 'Room'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'campsessions.session': {
            'Meta': {'ordering': "['title']", 'object_name': 'Session'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campsessions.Room']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['speakers.Speaker']", 'symmetrical': 'False'}),
            'time': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campsessions.Time']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'campsessions.time': {
            'Meta': {'ordering': "['time']", 'object_name': 'Time'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
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