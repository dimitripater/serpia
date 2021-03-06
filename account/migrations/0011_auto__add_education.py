# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Education'
        db.create_table(u'account_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'account', ['Education'])


    def backwards(self, orm):
        # Deleting model 'Education'
        db.delete_table(u'account_education')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'about_me': ('django.db.models.fields.TextField', [], {}),
            'branche': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['account.Branche']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Color']"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'has_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'account.branche': {
            'Meta': {'object_name': 'Branche'},
            'branche': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'account.color': {
            'Meta': {'object_name': 'Color'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'account.education': {
            'Meta': {'object_name': 'Education'},
            'education': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['account']