from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('tipoproductos', TipoProductoViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]