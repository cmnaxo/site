from asyncio.windows_events import NULL
import requests
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import *
from .models import *

from django.contrib.auth import authenticate, login as login_aut
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group

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

@login_required
def cart(request):
    
    usuario = request.user
    usuarioExtra = UsuarioExtra.objects.get(usuarioDjango = usuario)

    usuarioCarro = request.user.username
    carro = ItemsCarro.objects.filter(usuario = usuarioCarro)

    accum = 0

    for item in carro:
        item.total = item.cantidad * item.precio_producto
        item.save()
        accum += item.total
        

    usuario = request.user
    usuarioExtra = UsuarioExtra.objects.get(usuarioDjango = usuario)

    if usuarioExtra.suscripcion == True:
        total = round(accum - (accum * 0.05))

    else:
        total = accum

    descuento = round(accum * 0.05)
    usuarioExtra = UsuarioExtra.objects.all()

    datos = {
        'itemsCarro' : carro,
        'total' : total,
        'accum' : accum,
        'descuento' : descuento,
        'usuarioExtra' : usuarioExtra,
    }

    return render(request, 'app/cart.html', datos)

def eliminarCarro(request, id):
   
    carro = ItemsCarro.objects.get(id = id)
    codProd = carro.id_prod

    producto = Producto.objects.get(cod = int(codProd))
    producto.stock += carro.cantidad
    producto.save()
    carro.delete()

    return redirect(to="cart")

def aumentarCarro(request, id):
    carro = ItemsCarro.objects.get(id = id)
    carro.cantidad += 1
    carro.save()

    codProd = carro.id_prod
    producto = Producto.objects.get(cod = int(codProd))
    producto.stock -= 1
    producto.save()

    return redirect(to="cart")

def resetearCarro(request):

    usuarioCarro = request.user.username
    carro = ItemsCarro.objects.filter(usuario = usuarioCarro)

    lista = " "
    for item in carro:
        lista = "" + lista + item.nombre_producto + " (" + str(item.cantidad) + " )"

    cantidad_productos = len(carro)

    total = 0
    for item in carro:
        total += item.total

    cliente = request.user.username

    order = Orden()
    order.articulos = lista
    order.cantidad = cantidad_productos
    order.total = total
    order.estado_pedido = "Validación"
    order.cliente = cliente
    order.save()

    carro.delete()

    return redirect(to="cart")

@login_required
def donation(request):
    return render(request, 'app/donation.html')

@login_required
def success(request):
    carro = ItemsCarro.objects.all()
    carro.delete()

    messages.success(request, "¡Compra realizada correctamente!")

    return render(request, 'app/success.html')

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
            producto.save()

            usuarioCarro = request.user.username

            codigoProducto = request.POST.get('codigo_producto')
            carritoExistente = ItemsCarro.objects.filter(usuario = usuarioCarro, id_prod = codigoProducto)

            if carritoExistente:
                carro = ItemsCarro.objects.get(usuario = usuarioCarro, id_prod = codigoProducto)
                carro.cantidad += 1
                carro.total = carro.cantidad * carro.precio_producto
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

                return redirect(to="index-log")

        else:
            messages.success(request, "No hay stock disponible para este producto.")

    return render(request, 'app/index-log.html', datos)

def apiProductos(request):
    apiEndpoint = requests.get('https://rickandmortyapi.com/api/character').json()

    datos = {
        'apiEndpoint' : apiEndpoint['results']
    }

    return render(request, 'app/apiProductos.html', datos)

@login_required
def products(request):

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
            producto.save()

            usuarioCarro = request.user.username

            codigoProducto = request.POST.get('codigo_producto')
            carritoExistente = ItemsCarro.objects.filter(usuario = usuarioCarro, id_prod = codigoProducto)

            if carritoExistente:
                carro = ItemsCarro.objects.get(usuario = usuarioCarro, id_prod = codigoProducto)
                carro.cantidad += 1
                carro.total = carro.cantidad * carro.precio_producto
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

                return redirect(to="products")

        else:
            messages.success(request, "No hay stock disponible para este producto.")


    else:
            messages.success(request, "El producto selecciona no tiene stock disponible, vuelva a entrar más tarde.")

    return render(request, 'app/products.html', datos)

def registro(request):

    if request.method == 'POST':
        txtUser = request.POST.get('txtUser')
        txtEmail = request.POST.get('txtEmail')
        txtPassword = request.POST.get('txtPassword')
        txtNombre = request.POST.get('txtNombre')
        txtApellidos = request.POST.get('txtApellidos')
        txtRut = request.POST.get('txtRut')
        txtDv = request.POST.get('txtDv')
        txtDireccion = request.POST.get('txtDireccion')
        txtImagen = request.POST.get('txtImagen')

        try:
            usuario = User()
            usuario.username = txtUser
            usuario.first_name = txtNombre
            usuario.last_name = txtApellidos
            usuario.email = txtEmail
            usuario.password = txtPassword
            usuario.set_password(txtPassword)
            usuario.save()

            existsUser = User.objects.get(username=txtUser)

            usuarioExtra = UsuarioExtra()
            usuarioExtra.usuarioDjango = existsUser
            usuarioExtra.run = txtRut
            usuarioExtra.dv_run = txtDv
            usuarioExtra.direccion = txtDireccion
            usuarioExtra.suscripcion = False
            usuarioExtra.imagen = NULL
            usuarioExtra.save()

            group = Group.objects.get(name='Cliente')
            usuario.groups.add(group)

            access = authenticate(username=txtUser, password=txtPassword)
            if access is not None:
                login_aut(request, access)
                return redirect(to='index-log')

        except Exception as e:
            print("Error: " + str(e))
            messages.success(request, "El usuario ya existe.")

    return render(request, 'registration/registro.html')

@login_required
def suscribe(request):
    usuario = request.user
    usuarioExtra = UsuarioExtra.objects.get(usuarioDjango = usuario)

    usuarioExtra.suscripcion = True
    usuarioExtra.save()

    messages.success(request, "La suscripción se realizó exitosamente.")

    return redirect(to='perfil')

@login_required
def suscribete(request):

    user = request.user
    usuarioAll = UsuarioExtra.objects.all()
    
    #JSON > Recoge la variable productosAll, que a su vez contiene todas las variables del modelo (DB)
    datos = {
        'listaUsuarios' : usuarioAll,
        'user' : user
    }

    return render(request, 'app/suscribete.html', datos)

@login_required
def anularSuscripcion(request):
    usuario = request.user
    usuarioExtra = UsuarioExtra.objects.get(usuarioDjango = usuario)
    usuarioExtra.suscripcion = False
    usuarioExtra.save()
    messages.success(request, "Lamentamos que debas irte, esperamos tu apoyo nuevamente.")

    return redirect(to='perfil')

@login_required
def perfil(request):

    usuario = request.user
    usuarioExtra = UsuarioExtra.objects.get(usuarioDjango = usuario)

    historial = Orden.objects.filter(cliente = request.user.username)

    usuarioRun = UsuarioExtra.objects.all()

    datos = {
        'usuarioExtra' : usuarioExtra,
        'usuario' : usuario,
        'historial' : historial,
        'usuarioRun' : usuarioRun
    }

    return render(request, 'app/perfil.html', datos)

def cambiarFoto(request, rut):

    usuarios = UsuarioExtra.objects.get(run=rut)

    datos = {
        'form' : CambiarImg(instance=usuarios)
    }

    if request.method == 'POST':
        formulario = CambiarImg(data=request.POST, files=request.FILES, instance=usuarios)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La foto se actualizó exitosamente.")
            datos['form'] = formulario
            return redirect(to='perfil')

        return redirect(to='perfil')

    return render(request, 'app/perfil.html', datos)

@login_required
def tracking(request, codigo):
    usuario = request.user
    usuarioExtra = UsuarioExtra.objects.get(usuarioDjango = usuario)

    seguimiento = Orden.objects.get(codigo = codigo)

    historial = Orden.objects.filter(cliente = request.user.username)
    
    datos = {
        'seguimiento' : seguimiento,
        'usuarioExtra' : usuarioExtra,
        'usuario' : usuario,
        'historial' : historial
    }
    return render(request, 'app/tracking.html', datos)

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

@permission_required('app.change_orden')
def order(request):

    orden = Orden.objects.all()

    datos = {
        'orden' : orden,
    }

    return render(request, 'app/order.html', datos)

@permission_required('app.change_estado_orden')
def alterarEstado(request, code):

    estados = EstadoOrden.objects.all()

    orden = Orden.objects.get(codigo = code)

    if request.method == 'POST':
        estadoAlterado = request.POST.get('estados')
        orden.estado_pedido = estadoAlterado
        orden.save()

        return redirect(to='perfil')

    datos = {
        'estados' : estados,
        'orden' : orden,
    }

    return render(request, 'app/alterarEstado.html', datos)

