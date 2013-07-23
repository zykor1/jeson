# -*- coding: utf-8 *-*
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import json
from collections import namedtuple
from forms import JsonForm, TiposForm
from models import TJson



def  index(request):
	jsons = TJson.objects.all()
	return render_to_response('index.html', { 'lista': jsons }, context_instance=RequestContext(request))



def nuevoJson(request):
    if request.method=='POST':
        formulario = JsonForm(request.POST)
        if formulario.is_valid():
        	formulario.save()
        	return HttpResponseRedirect('/')
    else:
        formulario = JsonForm()
    return render_to_response('crud/nuevo.html', {'formulario':formulario}, context_instance=RequestContext(request))


def mostrarJson(request, id_json):
    tjson = TJson.objects.get(pk=id_json)
    return render_to_response('crud/mostrar.html', { 'dato': tjson }, context_instance=RequestContext(request))

def actualizarJson(request, id_jeson):
    tjson = TJson.objects.get(pk=id_jeson)
    if request.method=='POST':
        formulario = TiposForm(request.POST)
        if formulario.is_valid():
            jeson = json.loads(tjson.descripcion)
            jeson["contador"]["platino"] = request.POST.get('platino','')
            jeson["contador"]["oro"] = request.POST.get('oro','')
            jeson["contador"]["plata"] = request.POST.get('plata','')
            text = json.dumps(jeson)
            tjson.descripcion = text
            tjson.save()
            return HttpResponseRedirect('/')
    else:
        formulario = TiposForm()
    return render_to_response('crud/mostrar.html', { 'dato': tjson }, context_instance=RequestContext(request))
