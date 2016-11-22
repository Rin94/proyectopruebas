from django.shortcuts import render, redirect
from trabajos.forms import trabajosForm, lista_articulosForm


# Create your views here.
def nuevo(request):
    if request.method=='POST':
        form=trabajosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#')
    else:
        form=trabajosForm()
        form2=lista_articulosForm()
    return render(request,'addjob.html',{'form':form,'form2':form2,'funcion':'Nuevo'})

