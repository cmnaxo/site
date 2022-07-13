from .models import *

def procesadorUsuario(request):
    
    if request.user.is_authenticated:
        usuario = request.user
        usuarioExtend = UsuarioExtra.objects.get(usuarioDjango = usuario)
        suscripcionUsuario = usuarioExtend.suscripcion

        return {
            'suscripcionUsuario' : suscripcionUsuario
        }
    
    else:

        return {
            'usuario' : "vacío"
        }