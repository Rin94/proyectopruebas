from django.conf.urls import url
from tareas.views import editar,nuevo

urlpatterns=[
    url(r'^nuevo/$',nuevo,name="nueva_tarea"),
    url(r'^(?P<pk>[0-9]+)/editar/$', editar, name='editar_tarea'),
]