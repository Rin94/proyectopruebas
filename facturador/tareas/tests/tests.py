#from django.core.urlresolvers import resolve
#from django.http import HttpRequest
#from django.template.loader import render_to_string
from django.test import TestCase
from tareas.models import tareas

class ProbarTareas(TestCase):

    def tearUp(self):
        print ("Hola")

    def test_addTask(self):
        totalObj = tareas.objects.all()
        total= totalObj.count()
        tarea= tareas()
        tarea.nombre="Recuperacion de  archivos de disco duro"
        tarea.descripcion="Se busca los archivos importantes de un disco duro daniado"
        tarea.precio=999.99
        #total=tareas.objects.all()
        tarea.save()
        nuevo=tareas.objects.all()
        self.assertEqual(nuevo.count(),total+1)


