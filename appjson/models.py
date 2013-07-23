# -*- coding: utf-8 *-*
from django.db import models

from django.utils.translation import ugettext_lazy as _



class TJson (models.Model):
	nombre = models.CharField(max_length=45, blank=True, verbose_name=_(u'Nombre'))
	descripcion = models.TextField(verbose_name=_('Json'))

	def __unicode__(self):
		return '%s' %(self.nombre)