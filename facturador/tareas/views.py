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
            return redirect('/tareas/')
    else:
        form=formTareas()
    return render(request,'addtask.html',{'form':form,'funcion':'Nueva'})

def lista(request):
	tarea = tareas.objects.all()
	return render(request, 'listtask.html', {'tarea':tarea})

def eliminar(request, pk):
	mentor = tareas.objects.get(pk=pk)
	mentor.delete()
	return redirect('/tareas/')

def editar(request,pk):
    task=tareas.objects.get(pk=pk)
    if request.method=='POST':
        form=editFormTareas(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tareas/')
    else:
        form=editFormTareas(instance=task)
    return render(request,'addtask.html',{'form':form, 'funcion':'Actualizar'})

def eliminarPOST(request):
	id = request.POST.get('id_tareas','')
	mentor = tareas.objects.get(pk=id)
	mentor.delete()
	return redirect('/tareas/')