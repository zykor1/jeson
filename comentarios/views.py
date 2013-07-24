# -*- coding: utf-8 *-*
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import json
from collections import namedtuple
from forms import JComentarioForm
from models import JComentario



def  indexComentarios(request):
	jsons = JComentario.objects.all()
	return render_to_response('comentarios/index.html', { 'lista': jsons }, context_instance=RequestContext(request))



def nuevoComentario(request):
    if request.method=='POST':
        formulario = JComentarioForm(request.POST)
        if formulario.is_valid():
        	formulario.save()
        	return HttpResponseRedirect('/comentarios')
    else:
        formulario = JComentarioForm()
    return render_to_response('comentarios/nuevo.html', {'formulario':formulario}, context_instance=RequestContext(request))


def mostrarJson(request, id_json):
    tjson = JComentario.objects.get(pk=id_json)
    return render_to_response('comentarios/mostrar.html', { 'dato': tjson }, context_instance=RequestContext(request))


def agregarComentario(request, id_json):
    if request.method=='POST':
    	tjson = JComentario.objects.get(pk=id_json)
    	jeson = json.loads(tjson.comentario)
    	id_user = request.POST.get('user','')
    	datetime = request.POST.get('fecha','')
    	titulo = request.POST.get('titulo','')
    	comentario = request.POST.get('comentario','')
    	id_calificacion = "1"
    	id_userPK = request.POST.get('userFK','')
    	calificacion = request.POST.get('calificacion','')
    	row = '{ "id_user": %s, "datetime": "%s", "titulo": "%s", "comentario": "%s", "calificaciones" : [{"id":%s, "id_user"\
    	: %s, "calificacion": %s }] }' % (id_user, datetime, titulo, comentario, id_calificacion, id_userPK, calificacion)
    	nuevo = json.loads(row)
    	if tjson.id == 2:
    			for i in range(10000):
    				jeson["comentarios"].append(nuevo)
    	else:
    		jeson["comentarios"].append(nuevo)
    	text = json.dumps(jeson)
    	tjson.comentario = text
    	tjson.save()
        return HttpResponseRedirect('/comentarios')
    else:
    	return render_to_response('comentarios/agregar.html', {'dato':id_json}, context_instance=RequestContext(request))


def modificarComentario(request, id_promocion, id_json):
	tjson = JComentario.objects.get(pk=id_promocion)
	if request.method=='POST':
		jeson = json.loads(tjson.comentario)
		id_user = request.POST.get('user','')
		datetime = request.POST.get('fecha','')
		titulo = request.POST.get('titulo','')
		comentario = request.POST.get('comentario','')
		jeson["comentarios"][int(id_json)]["datetime"] = datetime
		jeson["comentarios"][int(id_json)]["titulo"] = titulo
		jeson["comentarios"][int(id_json)]["comentario"] = comentario
		text = json.dumps(jeson)
		tjson.comentario = text
		tjson.save()
		return HttpResponseRedirect('/comentarios/mostrar/'+id_promocion)
	else:
		return render_to_response('comentarios/modificar.html', {'dato':tjson, 'id_json':id_json}, context_instance=RequestContext(request))


def eliminarComentario(request, id_promocion, id_json):
	tjson = JComentario.objects.get(pk=id_promocion)
	jeson = json.loads(tjson.comentario)
	jeson["comentarios"].pop(int(id_json))
	text = json.dumps(jeson)
	tjson.comentario = text
	tjson.save()
	return HttpResponseRedirect('/comentarios/mostrar/'+id_promocion)