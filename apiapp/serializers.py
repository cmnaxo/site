from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from app.models import *

# Serializers define the API representation.
# Se encarga de realizar el CRUD desde el API hacía la BD

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' #No usar esto con el usuario

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'
        
class UsuarioExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioExtra
        fields = '__all__'

class TipoUsuarioExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuarioExtra
        fields = '__all__'