from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *

# Creamos templates de los formularios
# > Dejar la matriz hecha para despues solo realizarlo

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['cod', 'nombre', 'precio', 'stock', 'tipo', 'imagen']

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ['correo', 'contraseña', 'confirmar_contraseña']

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['cod_usuario', 'primer_nombre', 'primer_apellido', 'correo', 'tipo_usuario', 'imagen']

class SesionForm(forms.ModelForm):

    class Meta:
        model = Sesion
        fields = ['correo', 'contraseña']
