# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TJson'
        db.create_table(u'appjson_tjson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'appjson', ['TJson'])


    def backwards(self, orm):
        # Deleting model 'TJson'
        db.delete_table(u'appjson_tjson')


    models = {
        u'appjson.tjson': {
            'Meta': {'object_name': 'TJson'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        }
    }

    complete_apps = ['appjson']