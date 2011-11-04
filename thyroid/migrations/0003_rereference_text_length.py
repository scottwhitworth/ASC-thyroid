# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Reference.title'
        db.alter_column('thyroid_reference', 'title', self.gf('django.db.models.fields.CharField')(max_length=750))


    def backwards(self, orm):
        
        # Changing field 'Reference.title'
        db.alter_column('thyroid_reference', 'title', self.gf('django.db.models.fields.CharField')(max_length=125))


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
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['thyroid.Reference']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'thyroid.reference': {
            'Meta': {'object_name': 'Reference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '750'})
        }
    }

    complete_apps = ['thyroid']
