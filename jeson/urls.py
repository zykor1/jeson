from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'appjson.views.index'),
	url(r'^nuevo/$', 'appjson.views.nuevoJson'),
	url(r'^mostrar/(?P<id_json>\d+)$', 'appjson.views.mostrarJson'),
	url(r'^actualizar/(?P<id_jeson>\d+)$', 'appjson.views.actualizarJson'), 
	url(r'^comentarios/$', 'comentarios.views.indexComentarios'),
	url(r'^comentarios/nuevo/$', 'comentarios.views.nuevoComentario'),
	url(r'^comentarios/mostrar/(?P<id_json>\d+)$', 'comentarios.views.mostrarJson'),
	url(r'^comentarios/agregar/(?P<id_json>\d+)$', 'comentarios.views.agregarComentario'),
)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()