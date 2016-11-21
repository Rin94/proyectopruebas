#from django.core.urlresolvers import resolve
#from django.http import HttpRequest
#from django.template.loader import render_to_string
from django.test import TestCase
from tareas.models import tareas

class ProbarTareas(TestCase):

    def test_addTask(self):
        tarea= tareas()
        tarea.nombre="Recuperacion de  archivos de disco duro"
        tarea.descripcion="Se busca los archivos importantes de un disco duro daniado"
        tarea.precio=999.99
        total=tarea.objects.all()
        tarea.save()
        nuevo=tarea.objects.all()
        self.assertEqual(total.count()+1,nuevo)


