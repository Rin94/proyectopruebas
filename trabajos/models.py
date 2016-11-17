from __future__ import unicode_literals

from django.db import models
from clientes.models import clientes
from tareas.models import tareas
# Create your models here.
class trabajos(models.Model):
    cliente = models.ForeignKey('clientes', on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField('fecha_inicio', auto_now=False, auto_now_add=True)
    fehca_final = models.DateTimeField('fecha_fin', auto_now=True, auto_now_add=False)
    detalles = models.CharField('detalles', max_length= 120)

class lista_articulos(models.Model):
    trabajo = models.ForeignKey('trabajos', on_delete = models.CASCADE)
    tarea = models.ForeignKey('tareas', on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad')
    costo = models.FloatField('costo')
    detalles = models.CharField('detalles',max_length, null = True, blank = True)
