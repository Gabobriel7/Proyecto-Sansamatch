from django.db import models
from usuarios.models import Usuario
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Modelo para los matches entre usuarios
class Match(models.Model):
    usuario1 = models.ForeignKey(Usuario, related_name='match_usuario1', on_delete=models.CASCADE)
    usuario2 = models.ForeignKey(Usuario, related_name='match_usuario2', on_delete=models.CASCADE)
    tipo_match = models.CharField(max_length=20)  # Estudio, amistad o amoroso
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.usuario1} hizo match con {self.usuario2}"
    
    # Evita duplicar matches
    class Meta:
        unique_together = ('usuario1', 'usuario2') 

# Modelo para guardar los likes entre usuarios
class Like(models.Model):
    usuario_origen = models.ForeignKey(Usuario, related_name='likes_dados', on_delete=models.CASCADE)
    usuario_destino = models.ForeignKey(Usuario, related_name='likes_recibidos', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario_origen} dio like a {self.usuario_destino}"

    # Evitar duplicados en los likes
    class Meta:
        unique_together = ('usuario_origen', 'usuario_destino')

# Modelo para representar un grupo (de estudio o hobbies)
class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    usuarios = models.ManyToManyField(Usuario, related_name='grupos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

# Signal para detectar matches
@receiver(post_save, sender=Like)
def notificar_match(sender, instance, **kwargs):
    # Verificar si hay match (ambos se dieron like)
    if Like.objects.filter(usuario_origen=instance.usuario_destino, usuario_destino=instance.usuario_origen).exists():
        # Crear una notificación simple para el usuario que recibió el match
        instance.usuario_origen.notificaciones.create(
            mensaje=f"¡Tienes un match con {instance.usuario_destino.username}!"
        )
        instance.usuario_destino.notificaciones.create(
            mensaje=f"¡Tienes un match con {instance.usuario_origen.username}!"
        )
