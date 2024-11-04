"""
URL configuration for sansamatch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  
from django.conf.urls.static import static  
from usuarios.views import home
from usuarios import views as usuarios_views

# Definición de las rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),                                 # Ruta para el panel de administración
    path('home/', usuarios_views.home, name='home'),                 # Ruta de la Página Home
    path('', usuarios_views.pantalla_bienvenida, name='bienvenida'), # Página inicial (bienvenida)
    path('usuarios/', include('usuarios.urls')),                     # Incluir rutas de la app usuarios
    path('matches/', include('matches.urls')),                       # Incluir rutas de la app matches
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
                                      # Configuración para servir archivos multimedia en desarrollo
                                                  