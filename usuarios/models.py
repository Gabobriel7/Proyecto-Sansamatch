from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    carrera = models.CharField(max_length=100)
    sede = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    orientacion = models.CharField(max_length=10)
    intereses = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)