from django.conf.urls import url
from tareas.views import editar,nuevo,lista,eliminarPOST,eliminar

urlpatterns=[
    url(r'^nuevo/$',nuevo,name="nueva_tarea"),
    url(r'^$', lista, name="tareas"),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', eliminar, name='eliminar_tarea'),
    url(r'^(?P<pk>[0-9]+)/editar/$', editar, name='editar_tarea'),
    url(r'^eliminarPOST/$', eliminarPOST, name="eliminar_post"),
]