# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CodeExamples.slug'
        db.add_column(u'frontend_codeexamples', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='w', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CodeExamples.slug'
        db.delete_column(u'frontend_codeexamples', 'slug')


    models = {
        u'frontend.codeexamples': {
            'Meta': {'object_name': 'CodeExamples'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['frontend']