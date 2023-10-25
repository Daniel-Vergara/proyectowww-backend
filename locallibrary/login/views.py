from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario

class SignUpView(APIView):

    model = Usuario
    
    def post(self, request, format=None):

        data = self.request.data

        email = data['email']
        nombre = data['nombre']
        apodo = data['apodo']
        password = data['password']

        if Usuario.objects.filter(email=email).exists():
            return Response({'error': 'Este correo electrónico ya está en uso'})
        else:
            if Usuario.objects.filter(apodo=apodo).exist():
                return Response({'error': 'Este apodo ya está en uso'})
            else:
                Usuario.objects.create(email=email, nombre=nombre, apodo=apodo, password=password)
                return Response({'success': 'El usuario ha sido creado exitosamente'})


class LoginView(APIView):

    model = Usuario

    def post(self, request, format=None):

        data = self.request.data

        email = data['email']
        password = data['password']

        usuario = authenticate(email=email, password = password)
        login(self.request, usuario)
        return redirect('/cuenta')


