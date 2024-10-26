from django.db import models
from usuarios.models import Usuario

# Modelo para los matches entre usuarios
class Match(models.Model):
    usuario1 = models.ForeignKey(Usuario, related_name='match_usuario1', on_delete=models.CASCADE)
    usuario2 = models.ForeignKey(Usuario, related_name='match_usuario2', on_delete=models.CASCADE)
    tipo_match = models.CharField(max_length=20)  # Estudio, amistad o amoroso

# Modelo para guardar los likes entre usuarios
class Like(models.Model):
    usuario_origen = models.ForeignKey(Usuario, related_name='likes_dados', on_delete=models.CASCADE)
    usuario_destino = models.ForeignKey(Usuario, related_name='likes_recibidos', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    # Evitar duplicados en los likes
    class Meta:
        unique_together = ('usuario_origen', 'usuario_destino')

# Modelo para representar un grupo (de estudio o hobbies)
class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    usuarios = models.ManyToManyField(Usuario, related_name='grupos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
