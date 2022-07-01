from distutils.command.upload import upload
from django.db import models

# Para extensión modelo User de Django.
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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

class Registro(models.Model):
    cod_registro = models.IntegerField(null=False, primary_key=True)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.primer_nombre

    class Meta:
        db_table = 'db_registro'

class Usuario(models.Model):
    cod_usuario = models.IntegerField(null=False, primary_key=True)
    primer_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    tipo_usuario = models.IntegerField(choices=op_user)
    imagen = models.ImageField(upload_to="suscritos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.primer_nombre

    class Meta:
        db_table = 'db_usuario'

class Sesion(models.Model):
    cod_log = models.IntegerField(null=False, primary_key=True)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class ItemsCarro(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=60)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="items_carro", null=True)
    cantidad = models.IntegerField()
    total = models.IntegerField(blank=True)
    usuario = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'db_items_carro'

class Orden(models.Model):
    codigo = models.AutoField(primary_key=True)
    articulos = models.CharField(max_length=300)
    cantidad = models.IntegerField()
    total = models.IntegerField()
    estado_pedido = models.CharField(max_length=50)
    cliente = models.CharField(max_length=30)

    def __str__(self):
        return str(self.codigo)
    
    class Meta:
        db_table = 'db_orden'

class EstadoOrden(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return str(self.estado)
    
    class Meta:
        db_table = 'db_estado_orden'

class TipoUsuarioExtra(models.Model):
    tipo = models.CharField(max_length = 20)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_usuario'

class UsuarioExtra(models.Model):
    usuarioDjango = models.OneToOneField(User, on_delete = models.CASCADE)
    run = models.CharField(max_length = 9)
    dv_run = models.CharField(max_length = 1)
    direccion = models.CharField(max_length = 80)
    suscripcion = models.BooleanField()
    tipo_usuario = models.ForeignKey(TipoUsuarioExtra, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.usuarioDjango.username)

    class Meta:
        db_table = 'db_usuario_extra'
