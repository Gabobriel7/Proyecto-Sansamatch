from django.db import models
from usuarios.models import Usuario

class Match(models.Model):
    usuario1 = models.ForeignKey(Usuario, related_name='match_usuario1', on_delete=models.CASCADE)
    usuario2 = models.ForeignKey(Usuario, related_name='match_usuario2', on_delete=models.CASCADE)
    tipo_match = models.CharField(max_length=20)  # estudio, amistad o amoroso