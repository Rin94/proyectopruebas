from django import forms
from trabajos.models import trabajos
from trabajos.models import lista_articulos
from clientes.models import clientes
from tareas.models import tareas

class trabajosForm(forms.ModelForm):
    cliente=forms.ModelMultipleChoiceField(queryset=clientes.objects.all())
    detalles=forms.CharField(widget=forms.Textarea,max_length=120)
    fecha_final=forms.DateField(label='fecha aproximada')

    class Meta:
        model=trabajos
        fields=('cliente','fecha_inicio','fecha_final','detalles')


class lista_articulosForm(forms.ModelForm):
    tarea=forms.ModelMultipleChoiceField(queryset=tareas.objects.all())
    cantidad=forms.IntegerField(min_value=1,max_value=99)
    costo=forms.FloatField(min_value=1)
    class Meta:
        model=lista_articulos
        fields=('tarea', 'cantidad', 'costo')

