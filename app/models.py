from distutils.command.upload import upload
from tkinter import CASCADE
from unicodedata import decimal
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    cod = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_producto'

op_user = [
    [0, "Normal"],
    [1, "Suscrito"]
]

class Usuario(models.Model):
    cod_usuario = models.IntegerField(null=False, primary_key=True)
    primer_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    tipo_usuario = models.IntegerField(choices=op_user)
    imagen = models.ImageField(upload_to="suscritos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.primer_nombre, self.primer_apellido

    class Meta:
        db_table = 'db_usuario'

class ItemsCarro(models.Model):
    nombre_producto = models.CharField(max_length=60)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="items_carro", null=True)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'db_items_carro'
