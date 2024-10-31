from django.urls import path
from . import views

# Definición de las rutas (URLs) para la app 'matches'
urlpatterns = [
    path('swiping/', views.swiping, name='swiping'),             # Ruta para el swiping de perfiles
    path('crear-grupo/', views.crear_grupo, name='crear_grupo'), # Ruta para crear un grupo
    path('ver-grupos/', views.ver_grupos, name='ver_grupos'),    # Ruta para ver los grupos creados
    path('lista-likes/', views.lista_likes, name='lista_likes'), # Ruta para ver los likes y matches
]
