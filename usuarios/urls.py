from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

# Definición de las rutas (URLs) para la app 'usuarios'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('registro/', views.registro, name='registro'),                   # Ruta para el registro de usuario
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'), # Al cerrar sesión volver al home
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambiar-contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    path('historial/', views.historial_actividad, name='historial_actividad'),  
]
