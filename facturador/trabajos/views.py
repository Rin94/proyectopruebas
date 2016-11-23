from django.shortcuts import render, redirect
from trabajos.forms import trabajosForm, lista_articulosForm
from trabajos.models import trabajos,lista_articulos

# Create your views here.
def nuevo(request):
    if request.method=='POST':

        form=trabajosForm(request.POST)
        if form.is_valid():
            trabajo= trabajos.objects.create(
            cliente=request.POST.get('cliente',''),
            detalles=request.POST.get('detalles',''),
            )
            trabajo.save()
            lista_articulo=lista_articulos.objects.create(
                trabajo=trabajo.id,
                cantidad=request.POST.get('cantidad',''),
                costo=request.POST.get('costo',''),
                tarea=request.POST.get('tarea',''),


            )
            lista_articulo.save()


            return redirect('base.html')
    else:
        form=trabajosForm()
        form2=lista_articulosForm()
    return render(request,'addjob.html',{'form':form,'form2':form2,'funcion':'Nuevo'})

