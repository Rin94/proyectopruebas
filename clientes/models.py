from __future__ import unicode_literals

from django.db import models

# Create your models here.
class clientes(models.Model):
    first_name = models.CharField('first_name', max_length = 35)
    last_name = models.CharField('last_name', max_length = 45)
    gender = models.IntegerField('gender')
    email = models.EmailField('email', max_length = 60)
    phone_number = models.CharField('phone', max_length = 15)
    num_direccion = models.IntegerField('numero_casa')
    calle = models.CharField('calle', max_length = 45)
    colonia = models.CharField('colonia', max_length = 45)
    codigo_postal = models.IntegerField('codigo_postal')
    municipio = models.CharField('municipio', max_length = 30)
    estado = models.CharField('estado', max_length = 30)
    pais = models.CharField('pais', max_length = 30)
    detalles = models.CharField('detalles', max_length = 120, null = True, blank = True)
