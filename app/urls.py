from django.urls import path
from . import views  # Importar las vistas de la aplicación

urlpatterns = [
    # Ejemplo de una ruta a la vista principal
    path('', views.home, name='home'),
    # Añadir otras rutas según las vistas que hayas creado
]
