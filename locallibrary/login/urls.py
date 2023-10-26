from .views import SignUpView, LoginView
from django.urls import path


urlpatterns = [
    path('registro/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
]