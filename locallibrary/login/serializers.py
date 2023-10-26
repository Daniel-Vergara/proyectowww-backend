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
            'avatar',
        )

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'email',
            'password',
        )

class ModificarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'email',
            'nombre',
            'apodo',
            'password',
            'avatar',
            'is_active',
        )