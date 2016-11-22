from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from tareas.forms import formTareas, editFormTareas
from tareas.models import tareas

# Create your views here.
def nuevo(request):
    if request.method=='POST':
        form=formTareas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#')
    else:
        form=formTareas()
    return render(request,'addtask.html',{'form':form,'funcion':'Nueva'})

def editar(request,pk):
    task=tareas.objects.get(pk=pk)
    if request.method=='POST':
        form=editFormTareas(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('#')
    else:
        form=editFormTareas(instance=task)
    return render(request,'addtask.html',{'form':form, 'funcion':'Actualizar'})