from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    email = models.CharField(max_length=254)
    nombre = models.CharField(max_length=128)
    apodo = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.apodo
