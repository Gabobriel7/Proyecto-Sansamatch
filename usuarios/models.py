from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField

# Modelo de usuario personalizado que hereda de AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    numero_telefono = models.CharField(max_length=15, blank=True, null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)

    sede = models.CharField(max_length=50, choices=[
        ('Casa central', 'Casa central'),
        ('Viña del Mar', 'Viña del Mar'),
        ('Concepción', 'Concepción'),
        ('Vitacura', 'Vitacura'),
        ('San joaquin', 'San joaquin'),
    ], blank=True, null=True)

    sedes_preferidas = MultiSelectField(choices=[
        ('Casa central', 'Casa central'),
        ('Viña del Mar', 'Viña del Mar'),
        ('Concepción', 'Concepción'),
        ('Vitacura', 'Vitacura'),
        ('San joaquin', 'San joaquin'),
    ], blank=True, null=True)

    carrera = models.CharField(max_length=100, choices=[
        ('Ingeniería Civil', 'Ingeniería Civil'),
        ('I. Civil informatica', 'I. Civil informatica'),
        ('I. Civil Mecánica', 'I. Civil Mecánica'),
    ], blank=True, null=True)

    carreras_preferidas = MultiSelectField(choices=[
        ('Ingeniería Civil', 'Ingeniería Civil'),
        ('I. Civil informatica', 'I. Civil informatica'),
        ('I. Civil Mecánica', 'I. Civil Mecánica'),
    ], blank=True, null=True)

    preferencia = models.CharField(max_length=50, choices=[
        ('Amistad', 'Amistad'),
        ('Estudio', 'Estudio'),
        ('Relación', 'Relación'),
    ], blank=True, null=True)

    semestre = models.IntegerField(choices=[
        (1, '1º Semestre'),
        (2, '2º Semestre'),
        (3, '3º Semestre'),
        (4, '4º Semestre'),
        (5, '5º Semestre'),
        (6, '6º Semestre'),
        (7, '7º Semestre'),
        (8, '8º Semestre'),
        (9, '9º Semestre'),
        (10, '10º Semestre'),
    ], blank=True, null=True)
    
    genero = models.CharField(max_length=50, choices=[
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ], blank=True, null=True)

    genero_preferido = models.CharField(max_length=50, choices=[
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Todos', 'Todos'),
    ], blank=True, null=True, default='Todos')


# Modelo de Notificación
class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='notificaciones', on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    leida = models.BooleanField(default=False)  # Campo para marcar la notificación como leída
    fecha = models.DateTimeField(auto_now_add=True)