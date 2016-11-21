from django.contrib import admin
from clientes.models import clientes
from django.contrib.auth.models import  Permission
# Register your models here.

admin.site.register(clientes)
admin.site.register(Permission)