# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from models import TJson
from django import forms

class JsonForm(ModelForm):
	class Meta:
		model = TJson


class TiposForm(forms.Form):
    platino = forms.DecimalField(decimal_places=0)
    oro = forms.DecimalField(decimal_places=0)
    plata = forms.DecimalField(decimal_places=0)