# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from models import JComentario
from django import forms

class JComentarioForm(ModelForm):
	class Meta:
		model = JComentario
