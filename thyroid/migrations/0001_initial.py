# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Reference'
        db.create_table('thyroid_reference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('thyroid', ['Reference'])

        # Adding model 'Category'
        db.create_table('thyroid_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('order', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal('thyroid', ['Category'])

        # Adding model 'Diagnosis'
        db.create_table('thyroid_diagnosis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='diagnosis', to=orm['thyroid.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('thyroid', ['Diagnosis'])


    def backwards(self, orm):
        
        # Deleting model 'Reference'
        db.delete_table('thyroid_reference')

        # Deleting model 'Category'
        db.delete_table('thyroid_category')

        # Deleting model 'Diagnosis'
        db.delete_table('thyroid_diagnosis')


    models = {
        'thyroid.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'thyroid.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'diagnosis'", 'to': "orm['thyroid.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'thyroid.reference': {
            'Meta': {'object_name': 'Reference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        }
    }

    complete_apps = ['thyroid']
