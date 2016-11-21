from __future__ import unicode_literals

from django.db import models

from trabajos.models import trabajos, lista_articulos
# Create your models here.
class factura(models.Model):
    job = models.ForeignKey(trabajos, on_delete= models.CASCADE, unique = True)
    fecha_factura = models.DateField('fecha_factura', auto_now_add=True, auto_now=False)
    costo_total = models.FloatField('costo_total')
    detalles = models.CharField('detalles', max_length = 120, null = True, blank = True)

class articulos_facturados(models.Model):
    factura = models.ForeignKey(factura, on_delete= models.CASCADE, unique = True)
    orden = models.ForeignKey(lista_articulos,null = False, unique = True, primary_key = True)
