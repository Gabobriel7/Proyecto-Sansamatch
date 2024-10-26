from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

# Definición de las rutas (URLs) para la app 'usuarios'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('registro/', views.registro, name='registro'),                   # Ruta para el registro de usuario
    path('', views.home, name='home'),                                    # Ruta para la página principal (home)
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'), # Al cerrar sesión volver al home
]
