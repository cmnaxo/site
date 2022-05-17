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
    path('index-log', indexLog, name = "index-log"),
    path('login/', login, name = "login"),
    path('products/', products, name = "products"),
    path('register/', register, name = "register"),
    path('suscribe/', suscribe, name = "suscribe"),
    path('success/', success, name = "success"),
    path('agregar_producto/', agregar_producto, name = "agregar_producto"),
    path('modificarProducto/<cod>', modificarProducto, name = "modificarProducto"),
    path('eliminarProducto/<cod>', eliminarProducto, name = "eliminarProducto"),
    path('listarProductos/', listarProductos, name = "listarProductos"),
    path('agregarUsuario/', agregarUsuario, name = "agregarUsuario"),
    path('modificarUsuario/<cod_usuario>', modificarUsuario, name = "modificarUsuario"),
    path('eliminarUsuario/<cod_usuario>', eliminarUsuario, name = "eliminarUsuario"),
    path('listarUsuario/', listarUsuario, name = "listarUsuario"),
]