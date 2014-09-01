# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GroceryItem'
        db.create_table(u'core_groceryitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('unit', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['GroceryItem'])

        # Adding model 'List'
        db.create_table(u'core_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'core', ['List'])

        # Adding model 'ListItem'
        db.create_table(u'core_listitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grocery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.GroceryItem'])),
            ('purchased', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('root_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.List'])),
        ))
        db.send_create_signal(u'core', ['ListItem'])


    def backwards(self, orm):
        # Deleting model 'GroceryItem'
        db.delete_table(u'core_groceryitem')

        # Deleting model 'List'
        db.delete_table(u'core_list')

        # Deleting model 'ListItem'
        db.delete_table(u'core_listitem')


    models = {
        u'core.groceryitem': {
            'Meta': {'object_name': 'GroceryItem'},
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
            'purchased': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'root_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.List']"})
        }
    }

    complete_apps = ['core']