import re
from pkg_resources import require
import requests
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import *
from .models import *
from app.models import Producto

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

#El view se comporta como un controlador.
#Conecta con el modelo.

#QRUD Seccion > Listar
def home(request):
    productosAll = Producto.objects.all()
    
    #JSON > Recoge la variable productosAll, que a su vez contiene todas las variables del modelo (DB)
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/home.html', datos)

@permission_required('app.add_producto')
#CRUD Seccion > Agregar (CREATE)
def agregar_producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto agregado correctamente!"
        else:
            datos['form'] = formulario

    return render(request, 'app/productos/agregar_producto.html', datos)

@permission_required('app.change_producto')
#CRUD Seccion > Modificar (UPDATE)
def modificarProducto(request, cod):
    producto = Producto.objects.get(cod=cod)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Producto modificado correctamente!")
            return redirect(to=listarProductos)
        datos['form'] = formulario
    
    return render(request, 'app/productos/modificarProducto.html', datos)

@permission_required('app.view_producto')
#CRUD Seccion > Leer (READ)
def listarProductos(request):
    productosAll = Producto.objects.all()
    
    #JSON > Recoge la variable productosAll, que a su vez contiene todas las variables del modelo (DB)
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/productos/listarProductos.html', datos)

@permission_required('app.delete_producto')
#CRUD Seccion > Delete ()
def eliminarProducto(request, cod):
    producto = Producto.objects.get(cod=cod)
    producto.delete()
    messages.success(request, "¡Producto eliminado correctamente!")

    return redirect(to="listarProductos")

def aboutUs(request):
    return render(request, 'app/about-us.html')

#CarritoCompra : LISTO
@login_required
def cart(request):
    
    usuarioCarrito = request.user.username
    carritoAll = ItemsCarro.objects.filter(usuario = usuarioCarrito)
    contadorGlobal = 0

    for Producto in carritoAll:
        Producto.total = Producto.precio_producto * Producto.cantidad
        Producto.save()
        contadorGlobal = contadorGlobal + Producto.total

    usuario = request.user
    usuarioExtra = UsuarioExtra.objects.get(usuarioDjango = usuario)

    if usuarioExtra.suscripcion == True:
        total = round(contadorGlobal -  (contadorGlobal * 0.05) )

    else:
        total = round(contadorGlobal)

    datos = {
        'ItemsCarrito' : carritoAll,
        'contadorGlobal' : contadorGlobal,
        'total' : total
    }

    return render(request, 'app/cart.html', datos)

#Acumulador del carro / cantidad
#AumentarCarrito: LISTO
@permission_required('app.add_producto')
def AumentarCarrito(request, id_prod):
    carro = ItemsCarro.objects.get(id_prod=id_prod)
    carro.cantidad += 1
    carro.save()

    producto = Producto.objects.get(cod = int(id_prod))
    producto.stock -= 1
    producto.save()

    return redirect(to='cart')

#CRUD Carro > Delete
#EliminarDeCarrito: LISTO
@permission_required('app.delete_producto')
def EliminarDeCarrito(request, id_prod):
    carro = ItemsCarro.objects.get(id_prod=id_prod)
    carro.cantidad = carro.cantidad - 1

    if carro.cantidad > 0:
        carro.save()

    else:
        carro.delete()

    producto = Producto.objects.get(codigo=int(id_prod))
    producto.stock += 1
    producto.save()

    return redirect(to='cart')

#ResetCarrito: LISTO
@permission_required('app.delete_producto')
def ResetCarrito(request):
    
    usuarioCarrito = request.user.username
    carritoAll = ItemsCarro.objects.filter(usuario = usuarioCarrito)

    lista_productos = " "
    for producto in carritoAll:
        lista_productos = "" + lista_productos + producto.nombre_producto + " (" + str(producto.cantidad) + ") "

    cantidad_productos = len(carritoAll)

    precio_total = 0
    for producto in carritoAll:
        precio_total = precio_total + producto.total

    cliente = request.user.username

    orden = Orden()
    orden.articulos = lista_productos
    orden.cantidad = cantidad_productos
    orden.total = precio_total
    orden.estado_pedido = "Orden recibida"
    orden.cliente = cliente
    orden.save()

    carritoAll.delete()

    return redirect(to='cart')

@login_required
def donation(request):
    return render(request, 'app/donation.html')

@login_required
def success(request):
    carro = ItemsCarro.objects.all()
    carro.delete()

    return render(request, 'app/success.html')

#Pendiente
@login_required
def historial(request):
    
    historial = Orden.objects.filter(cliente=request.user.username)
    
    datos = {
        'listaOrden' : historial
    }

    return render(request, 'app/historial.html', datos)

@login_required
def indexLog(request):
    apiProductos = requests.get('http://127.0.0.1:8000/api/productos/').json()
    productosAll = Producto.objects.all()

    #JSON > Recoge la variable productosAll, que a su vez contiene todas las variables del modelo (DB)
    datos = {
        'listaProductos' : productosAll,
        'listaApiProductos' : apiProductos
    }

    if request.method == 'POST':
        cod = request.POST.get('codigo_producto')
        producto = Producto.objects.get(cod=int(cod))

        if producto.stock > 0:
            producto.stock -= 1
            carritoCantidad = 0
            producto.save()

            codigoProducto = request.POST.get('codigo_producto')
            carritoExistente = ItemsCarro.objects.filter(id_prod=codigoProducto)

            if carritoExistente:
                carro = ItemsCarro.objects.get(id_prod=codigoProducto)
                carro.cantidad = carro.cantidad + 1
                carro.save()

            else:
                carro = ItemsCarro()
                carro.imagen = request.POST.get('imagen')     
                carro.nombre_producto = request.POST.get('nombre_producto')
                carro.precio_producto = request.POST.get('precio_producto')
                carro.id_prod = request.POST.get('codigo_producto')
                carro.cantidad = 1
                carro.total = 0
                carro.usuario = request.user.username
                carro.save()

                return redirect(to='index-log')

        else:
            messages.success(request, "No hay stock disponible para este producto.")

    return render(request, 'app/index-log.html', datos)

def apiProductos(request):
    apiEndpoint = requests.get('https://rickandmortyapi.com/api/character').json()

    datos = {
        'apiEndpoint' : apiEndpoint['results']
    }

    return render(request, 'app/apiProductos.html', datos)

def login(request):
    datos = {
        'form': SesionForm()
    }

    return render(request, 'app/login.html', datos)

#LISTO
@login_required
def products(request, cod):

    producto = Producto.objects.get(cod=cod)
    
    #JSON > Recoge la variable productosAll, que a su vez contiene todas las variables del modelo (DB)
    datos = {
        'producto' : producto
    }
    
    if request.method == 'POST':
        carro = ItemsCarro()
        #Rellenamos el carro con los datos que vienen de POST
        carro.imagen = request.POST.get('imagen')
        carro.nombre_producto = request.POST.get('nombre_producto')
        carro.precio_producto = request.POST.get('precio_producto')
        carro.cantidad = request.POST.get('cantidad_producto')
        carro.save()

    return render(request, 'app/products.html', datos)

def register(request):
    datos = {
        'form': RegistroForm()
    }

    return render(request, 'app/register.html', datos)

def registro(request):
    datos = {
        'form' : RegistroUserForm()
    }

    if request.method == 'POST':
        formulario = RegistroUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="login")
        datos["form"] = formulario

    return render(request, 'registration/registro.html', datos)

@login_required
def suscribe(request):
    usuarioAll = Usuario.objects.all()
    
    #JSON > Recoge la variable productosAll, que a su vez contiene todas las variables del modelo (DB)
    datos = {
        'listaUsuarios' : usuarioAll
    }

    if request.POST:
        usuario = request.user
        usuarioExtra = usuarioExtra.objects.get(usuarioDjango = usuario)
        usuarioExtra.suscripcion = True
        usuarioExtra.save()
        messages.success(request, "La suscripción se realizó exitosamente.")

    return render(request, 'app/suscribe.html', datos)

def cancelarSuscripcion(request):
    usuario = request.user
    usuarioExtra = UsuarioExtra.objects.get(usuarioDjango = usuario)
    usuarioExtra.suscripcion = False
    usuarioExtra.save()
    messages.success(request, "Lamentamos que debas irte, esperamos tu apoyo nuevamente.")

    datos = {
        'usuarioExtra' : usuarioExtra,
        'usuario' : usuario
    }

    return render(request, 'app')

@permission_required('app.add_usuario')
#CRUD Seccion > Agregar (CREATE)
def agregarUsuario(request):
    datos = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario agregado correctamente!"
        else:
            datos['form'] = formulario

    return render(request, 'app/usuarios/agregarUsuario.html', datos)

@permission_required('app.change_usuario')
#CRUD Seccion > Modificar (UPDATE)
def modificarUsuario(request, cod_usuario):
    usuario = Usuario.objects.get(cod_usuario=cod_usuario)
    datos = {
        'form' : UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Usuario modificado correctamente!")
            return redirect(to=listarUsuario)
        datos['form'] = formulario
    
    return render(request, 'app/usuarios/modificarUsuario.html', datos)

@permission_required('app.view_usuario')
#CRUD Seccion > Leer (READ)
def listarUsuario(request):
    usuarioAll = Usuario.objects.all()
    
    #JSON > Recoge la variable productosAll, que a su vez contiene todas las variables del modelo (DB)
    datos = {
        'listaUsuarios' : usuarioAll
    }

    return render(request, 'app/usuarios/listarUsuario.html', datos)

@permission_required('app.delete_usuario')
#CRUD Seccion > Delete ()
def eliminarUsuario(request, cod_usuario):
    usuario = Usuario.objects.get(cod_usuario=cod_usuario)
    usuario.delete()
    messages.success(request, "¡Usuario eliminado correctamente!")

    return redirect(to="listarUsuario")

@login_required
def despacho(request):
    return render(request, 'app/despacho.html')

def ordenUsuario(request):

    orden = Orden.objects.all()

    estados = EstadoOrden.objects.all()

    datos = {
        'orden' : orden,
        'estados' : estados
    }

    return render(request, '')

def CambiarEstadoOrden(request, codigoOrden):

    mensaje = " "

    estados = EstadoOrden.objects.all()
    orden = Orden.objects.get(codigo = codigoOrden)

    if request.method == 'POST':
        estadoNuevo = request.POST.get('estados')
        orden.estado_pedido = estadoNuevo
        orden.save()
        mensaje = "Estado de pedido actualizado. ✅"

    retorno = {
        'estados' : estados,
        'orden' : orden,
        'mensaje' : mensaje
    }

    return render(request, ) #TERMINAR

def seguimiento (request):
    return render(request, 'app/seguimiento.html')