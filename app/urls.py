from django.urls import path
from .views import *

#Nuestro modulo debe ser cargado en el principal

urlpatterns = [
    path('', home, name = "home"),
    path('about-us/', aboutUs, name = "about-us"),
    path('cart/', cart, name = "cart"),
    path('despacho/', despacho, name = "despacho"),
    path('donation/', donation, name = "donation"),
    path('historial/', historial, name = "historial"),
    path('tracking/<codigo>/', tracking, name = "tracking"),
    path('order/', order, name = "order"),
    path('index-log', indexLog, name = "index-log"),
    path('products/', products, name = "products"),
    path('apiProductos/', apiProductos, name = "apiProductos"),
    path('registro/', registro, name = "registro"),
    path('suscribe/', suscribe, name = "suscribe"),
    path('suscribete/', suscribete, name = "suscribete"),
    path('anularSuscripcion/', anularSuscripcion, name = "anularSuscripcion"),
    path('success/', success, name = "success"),
    path('agregar_producto/', agregar_producto, name = "agregar_producto"),
    path('modificarProducto/<cod>', modificarProducto, name = "modificarProducto"),
    path('eliminarProducto/<cod>', eliminarProducto, name = "eliminarProducto"),
    path('listarProductos/', listarProductos, name = "listarProductos"),
    path('perfil/', perfil, name = "perfil"),
    path('cambiarFoto/<rut>/', cambiarFoto, name="cambiarFoto"), 
    path('agregarUsuario/', agregarUsuario, name = "agregarUsuario"),
    path('modificarUsuario/<cod_usuario>', modificarUsuario, name = "modificarUsuario"),
    path('eliminarUsuario/<cod_usuario>', eliminarUsuario, name = "eliminarUsuario"),
    path('listarUsuario/', listarUsuario, name = "listarUsuario"),
    path('eliminarCarro/<id>/', eliminarCarro, name = "eliminarCarro"),
    path('aumentarCarro/<id>/', aumentarCarro, name = "aumentarCarro"),
    path('resetearCarro/', resetearCarro, name = "resetearCarro"),
    path('alterarEstado/<code>/', alterarEstado, name = "alterarEstado"),
]