from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer, LoginSerializer, ModificarUsuarioSerializer, InactivarUsuarioSerializer


def get_usuario(request):

    session_id = request.COOKIES.get('sessionid')

    try:
        session = Session.objects.get(session_key=session_id)
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=user_id)
    except (Session.DoesNotExist, User.DoesNotExist):
        user = None

    return user


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
                user = User.objects.create_user(username=email, password=password)
                Usuario.objects.create(email=email, nombre=nombre, apodo=apodo, password=password, avatar=avatar)
                return Response({'success': 'El usuario ha sido creado exitosamente'}) 
            

class LoginView(APIView):

    serializer_class = LoginSerializer

    def post(self, request, format=None):

        data = self.request.data

        email = data['email']
        password = data['password']

        usuario = authenticate(username=email, password=password)

        if usuario is not None:

            if Usuario.objects.get(email=email).is_active:

                login(request, usuario)

                usuariologeado = Usuario.objects.get(email = email)

                nombre = usuariologeado.nombre
                apodo = usuariologeado.apodo
                avatar = usuariologeado.avatar
                is_active = usuariologeado.is_active
                return Response(({'success':'Usuario autenticado exitosamente', "email": email, "nombre": nombre, "apodo": apodo, "password": password, "avatar": avatar, "Activo":is_active}))
            
            else: Response({'error': 'Usuario inactivo'})
        
        else:
            return Response({'error': 'Correo o contraseña incorrectos'})
    
class ModificarUsuarioView(APIView):

    serializer_class = ModificarUsuarioSerializer
    queryset = Usuario.objects.all()

    def get(self, request, format=None):

        usuario = get_usuario(request)
        email = Usuario.objects.get(email = usuario).email
        nombre = Usuario.objects.get(email = usuario).nombre
        apodo = Usuario.objects.get(email = usuario).apodo
        password = Usuario.objects.get(email = usuario).password
        is_active = Usuario.objects.get(email = usuario).password

        mensaje = "email: {}\n nombre: {}\n apodo: {}\n password: {}\n Usuario activo: {}\n".format(email, nombre, apodo, password, is_active)
        return Response({'sucess':mensaje})


    def put(self, request, format=None):

        data = self.request.data

        usuario = get_usuario(request)
        email = Usuario.objects.get(email = usuario).email
        nombre = data['nombre']
        apodo = data['apodo']
        password = data['password']
        avatar = data['avatar']
        
        if Usuario.objects.filter(apodo=apodo).exists():
            return Response({'error': 'Este apodo ya está en uso'})
        else:
            Usuario.objects.filter(email=email).update(nombre=nombre, apodo=apodo, password=password, avatar=avatar)
            return Response({'success': 'Se han actualizado los datos del usuario'})
        
class InactivarUsuarioView(APIView):

    serializer_class = InactivarUsuarioSerializer

    def put(self, request, format=None):

        data = self.request.data
        usuario = get_usuario(request)
        email = Usuario.objects.get(email = usuario).email

        is_active = data['is_active']

        if not is_active:
            Usuario.objects.filter(email=email).update(is_active = False)
            return Response({'success': 'El Usuario ha sido inhabilitado'})
        else:
            return Response({'error': 'No se inhabilitado al usuario'})
    
    
        


