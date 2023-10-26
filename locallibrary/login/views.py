from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer, LoginSerializer, ModificarUsuarioSerializer


class SignUpView(APIView):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
    def post(self, request, format=None):

        data = self.request.data

        email = data['email']
        nombre = data['nombre']
        apodo = data['apodo']
        password = data['password']
        avatar = data['avatar']

        if Usuario.objects.filter(email=email).exists():
            return Response({'error': 'Este correo electrónico ya está en uso'})
        else:
            if Usuario.objects.filter(apodo=apodo).exists():
                return Response({'error': 'Este apodo ya está en uso'})
            else:
                Usuario.objects.create(email=email, nombre=nombre, apodo=apodo, password=password, avatar=avatar)
                return Response({'success': 'El usuario ha sido creado exitosamente'}) 
            

class LoginView(APIView):

    serializer_class = LoginSerializer

    def post(self, request, format=None):

        data = self.request.data

        email = data['email']
        password = data['password']

        usuario = authenticate(email=email, password=password)
        login(request, usuario)
        return redirect('/api/modificar')
    
class ModificarUsuarioView(APIView):

    serializer_class = ModificarUsuarioSerializer
    queryset = Usuario.objects.all()

    def put(self, request, format=None):

        data = self.request.data

        email = data["email"]
        nombre = data['nombre']
        apodo = data['apodo']
        password = data['password']
        avatar = data['avatar']


        if Usuario.objects.filter(apodo=apodo).exists():
            return Response({'error': 'Este apodo ya está en uso'})
        else:
            Usuario.objects.filter(email=email).update(nombre=nombre, apodo=apodo, password=password, avatar=avatar)
            return Response({'success': 'Se han actualizado los datos del usuario'})


