from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'facturador.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^tareas/', include('tareas.urls')),
    url(r'^trabajos/', include('trabajos.urls')),

]
