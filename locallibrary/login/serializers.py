from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'email',
            'nombre',
            'apodo',
            'password',
        )

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'email',
            'password',
        )