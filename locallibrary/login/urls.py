from .views import SignUpView, LoginView, ModificarUsuarioView, InactivarUsuarioView
from django.urls import path


urlpatterns = [
    path('registro/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('modificar/',ModificarUsuarioView.as_view()),
    path('inactivar_usuario/', InactivarUsuarioView.as_view())
]