from django.conf.urls import url
from clientes.views import editar,nuevo,lista,eliminar

urlpatterns=[
    url(r'^nuevo/$',nuevo,name="nuevo_cliente"),
    url(r'^(?P<pk>[0-9]+)/editar/$', editar, name='editar_cliente'),
    url(r'^$', lista, name="clientes"),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', eliminar, name='eliminar_cliente'),
]