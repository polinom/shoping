# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ListItem.items'
        db.add_column(u'core_listitem', 'items',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ListItem.items'
        db.delete_column(u'core_listitem', 'items')


    models = {
        u'core.groceryitem': {
            'Meta': {'object_name': 'GroceryItem'},
            'favorit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'unit': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.list': {
            'Meta': {'object_name': 'List'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'crated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.listitem': {
            'Meta': {'object_name': 'ListItem'},
            'grocery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.GroceryItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'purchased': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'root_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.List']"})
        }
    }

    complete_apps = ['core']