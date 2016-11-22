from django import forms
from clientes.models import clientes

class FormClientes(forms.ModelForm):
    CHOICES = (
        ('1', 'Hombre'),
        ('2', 'Mujer'),

    )
    gender = forms.ChoiceField(widget=forms.Select, choices=CHOICES,label='genero')
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15,label="telefono")
    codigo_postal = forms.IntegerField(max_value=9999,label="CP")
    #detalles = forms.CharField(widget=forms.Textarea, max_length=120)
    first_name=forms.CharField(label='nombre')
    last_name=forms.CharField(label='apellidos')
    num_direccion=forms.IntegerField(label='numero',max_value=99999)

    class Meta:

        model= clientes
        fields=('first_name','last_name','gender','email','phone_number','num_direccion','calle','colonia',
                'codigo_postal','municipio','estado')



class EditFormClientes(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15,label='telefono')
    codigo_postal = forms.IntegerField(max_value=9999,label='CP')
    #detalles = forms.CharField(widget=forms.Textarea, max_length=120,required=False)
    num_direccion = forms.IntegerField(label='numero', max_value=99999)

    class Meta:

        model= clientes
        fields=('email','phone_number','num_direccion','calle','colonia',
                'codigo_postal','municipio','estado')