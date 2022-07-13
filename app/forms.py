from dataclasses import fields
from django import forms

from django.forms import ModelForm, ValidationError
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

# Creamos templates de los formularios
# > Dejar la matriz hecha para despues solo realizarlo

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=5)

    class Meta:
        model = Producto
        fields = ['cod', 'nombre', 'precio', 'stock', 'tipo', 'imagen']

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ['correo', 'contraseña']

class RegistroUserForm(UserCreationForm):
    
    username = forms.CharField(min_length=5, max_length=20)
    first_name = forms.CharField(min_length=5, max_length=20)
    last_name = forms.CharField(min_length=5, max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=5, max_length=15)
    password2 = forms.CharField(min_length=5, max_length=15)

    class meta:
        model = User
        fields = ['username','first_name','last_name','correo','password1','password2']

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['cod_usuario', 'primer_nombre', 'primer_apellido', 'correo', 'tipo_usuario', 'imagen']

class SesionForm(forms.ModelForm):

    class Meta:
        model = Sesion
        fields = ['correo', 'contraseña']

class OrdenForm(forms.ModelForm): 

    class Meta:
        model = Orden
        fields = ['codigo', 'articulos', 'cantidad', 'total', 'estado_pedido', 'cliente']

class CambiarImg(ModelForm):

    class Meta:
        
        model = UsuarioExtra
        fields = ['imagen']