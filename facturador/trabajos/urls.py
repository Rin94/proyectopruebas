from django.conf.urls import url
from trabajos.views import nuevo

urlpatterns=[
    url(r'^nuevo/$',nuevo,name="nuevo_trabajo"),
    #url(r'^(?P<pk>[0-9]+)/editar/$', editar, name='editar_cliente'),
]