from dataclasses import fields
from multiprocessing.sharedctypes import Value
from django import forms
from django.forms import ModelForm, ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

# Creamos templates de los formularios
# > Dejar la matriz hecha para despues solo realizarlo

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=5)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        exists = Producto.objects.filter(nombre__iexact=nombre).exists()

        if exists:
            raise ValidationError("Este nombre ya está registrado anteriormente, prueba uno nuevo.")

        return nombre

    class Meta:
        model = Producto
        fields = ['cod', 'nombre', 'precio', 'stock', 'tipo', 'imagen']

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ['correo', 'contraseña']

class RegistroUserForm(UserCreationForm):
    pass

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['cod_usuario', 'primer_nombre', 'primer_apellido', 'correo', 'tipo_usuario', 'imagen']

class SesionForm(forms.ModelForm):

    class Meta:
        model = Sesion
        fields = ['correo', 'contraseña']
