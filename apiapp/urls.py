from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('tipoproductos', TipoProductoViewSet)
router.register('usuario', UsuarioExtraViewSet)
router.register('tipousuarioextra', TipoUsuarioExtraViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]