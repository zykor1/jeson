# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JComentario'
        db.create_table(u'comentarios_jcomentario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'comentarios', ['JComentario'])


    def backwards(self, orm):
        # Deleting model 'JComentario'
        db.delete_table(u'comentarios_jcomentario')


    models = {
        u'comentarios.jcomentario': {
            'Meta': {'object_name': 'JComentario'},
            'comentario': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['comentarios']