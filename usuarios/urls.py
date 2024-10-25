from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('registro/', views.registro, name='registro'),
    path('', views.home, name='home'),  # Ruta para la página principal
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
