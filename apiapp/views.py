from django import views
from app.models import *
from .serializers import *
from rest_framework import viewsets

#Se encarga de mostrar el QUERY en el API

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class UsuarioExtraViewSet(viewsets.ModelViewSet):
    queryset = UsuarioExtra.objects.all()
    serializer_class = UsuarioExtraSerializer

class TipoUsuarioExtraViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuarioExtra.objects.all()
    serializer_class = TipoUsuarioExtraSerializer
