from django.contrib.auth.models import AbstractUser
from django.db import models

# Modelo de usuario personalizado que hereda de AbstractUser
class Usuario(AbstractUser):
    carrera = models.CharField(max_length=100)
    sede = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    orientacion = models.CharField(max_length=10)
    intereses = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

# Modelo de Notificación
class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='notificaciones', on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    leida = models.BooleanField(default=False)  # Campo para marcar la notificación como leída
    fecha = models.DateTimeField(auto_now_add=True)