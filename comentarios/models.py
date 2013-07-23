# -*- coding: utf-8 *-*
from django.db import models

from django.utils.translation import ugettext_lazy as _



class JComentario (models.Model):
	comentario = models.TextField(verbose_name=_('Json'))

	def __unicode__(self):
		return '%s' %(self.nombre)