from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from clientes.models import clientes
from clientes.views import nuevo

# Create your tests here.

class ProbarCliente(TestCase):

    def agregarCliente(self):
        cliente=clientes()
        cliente.first_name="Thomas"
        cliente.last_name="Thomasin"
        cliente.email="tomas87@gmail.com"
        cliente.phone_number="492123203"
        cliente.calle="En un lugar"





