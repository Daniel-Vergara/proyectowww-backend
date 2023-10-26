from .views import SignUpView, LoginView, ModificarUsuarioView
from django.urls import path


urlpatterns = [
    path('registro/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('modificar/',ModificarUsuarioView.as_view()),
]