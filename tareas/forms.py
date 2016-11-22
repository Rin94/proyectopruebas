from tareas.models import tareas
from django import forms

class formTareas(forms.ModelForm):
    nombre=forms.CharField(max_length=60,required=True)
    precio=forms.FloatField(min_value=1, max_value=999999.99)
    descripcion=forms.CharField(widget=forms.Textarea,max_length=120)

    class Meta:
        model=tareas
        fields=('nombre','precio','descripcion')




class editFormTareas(forms.ModelForm):
    nombre=forms.CharField(max_length=60,required=True)
    precio=forms.FloatField(min_value=1, max_value=999999.99)
    descripcion=forms.CharField(widget=forms.Textarea,max_length=120)

    class Meta:
        model=tareas
        fields=('nombre','precio','descripcion')