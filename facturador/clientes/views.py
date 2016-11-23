from django.shortcuts import render, redirect
from clientes.forms import FormClientes, EditFormClientes
from clientes.models import clientes

# Create your views here.
def nuevo(request):
    if request.method=='POST':
        form=FormClientes(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
    else:
        form=FormClientes()
    return render(request,'addcliente.html',{'form':form,'funcion':'Nuevo'})

def lista(request):
	cliente = clientes.objects.all()
	return render(request, 'listclients.html', {'cliente':cliente})

def eliminar(request, pk):
	cliente = clientes.objects.get(pk=pk)
	cliente.delete()
	return redirect('/clientes/')



def editar(request,pk):
    customer=clientes.objects.get(pk=pk)
    if request.method=='POST':
        form=EditFormClientes(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
    else:
        form=EditFormClientes(instance=customer)
    return render(request,'addcliente.html',{'form':form, 'funcion':'Actualizar'})

