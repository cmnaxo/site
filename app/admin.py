from django.contrib import admin
from .models import *

# Register your models here.

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ['tipo']
    search_fields = ['tipo']
    list_editable = ['tipo']
    list_filter = ['tipo']
    list_per_page = ['tipo']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['cod', 'nombre', 'precio', 'stock', 'tipo', 'imagen', 'created_at', 'updated_at']
    search_fields = ['cod']
    list_editable = ['precio']
    list_filter = ['tipo', 'imagen']
    list_per_page = 5

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['cod_usuario', 'primer_nombre', 'primer_apellido', 'correo' ,'tipo_usuario', 'imagen' ,'created_at', 'updated_at']
    search_fields = ['cod_usuario', 'primer_apellido']
    list_editable = ['correo', 'tipo_usuario']
    list_filter = ['tipo_usuario']
    list_per_page = 5

class CarroAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'precio_producto', 'p_final', 'imagen', 'created_at']
    search_fields = ['nombre_producto']
    list_editable = ['precio_producto']
    list_filter = ['nombre_producto']
    list_per_page = 5


admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ItemsCarro)
