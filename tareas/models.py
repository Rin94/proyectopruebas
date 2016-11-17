from __future__ import unicode_literals

from django.db import models

# Create your models here.
def tareas(models.Model):
    nombre = models.CharField('nombre', max_length = 60)
    precio = models.FloatField('precio')
    descripcion = models.CharField('descripcion', max_length = 120)
    detalles = models.CharField('detalles', max_length = 120, null = True, blank = True)
