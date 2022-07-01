from django.contrib import admin

from app.forms import ProductoForm
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['cod', 'nombre', 'precio', 'stock', 'tipo', 'imagen', 'created_at', 'updated_at']
    search_fields = ['cod']
    list_editable = ['precio']
    list_filter = ['tipo', 'imagen']
    list_per_page = 5

    #El admin ocupa las validaciones de nuestro formulario
    form = ProductoForm

class RegistroAdmin(admin.ModelAdmin):
    list_display = ['cod_registro', 'correo', 'contraseña', 'created_at', 'updated_at']
    search_fields = ['cod_registro', 'correo']
    list_editable = ['correo', 'contraseña']
    list_filter = ['created_at']
    list_per_page = 5

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['cod_usuario', 'primer_nombre', 'primer_apellido', 'correo' ,'tipo_usuario', 'imagen' ,'created_at', 'updated_at']
    search_fields = ['cod_usuario']
    list_editable = ['correo', 'tipo_usuario']
    list_filter = ['tipo_usuario']
    list_per_page = 5

class CarroAdmin(admin.ModelAdmin):
    list_display = ['id_prod', 'nombre_producto', 'precio_producto', 'imagen', 'cantidad', 'total']
    search_fields = ['nombre_producto']
    list_editable = ['precio_producto']
    list_filter = ['nombre_producto']
    list_per_page = 5

class SesionAdmin(admin.ModelAdmin):
    list_display = ['cod_log', 'correo', 'contraseña', 'created_at', 'updated_at']
    search_fields = ['cod_log', 'correo']
    list_editable = ['correo', 'contraseña']
    list_filter = ['created_at']
    list_per_page = 5

class OrdenAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'articulos', 'cantidad', 'total', 'estado_pedido', 'cliente']
    search_fields = ['codigo', 'cliente']
    list_per_page = 5

admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ItemsCarro, CarroAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Sesion, SesionAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(EstadoOrden)
admin.site.register(UsuarioExtra)
admin.site.register(TipoUsuarioExtra)

