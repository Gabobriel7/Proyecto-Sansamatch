from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import EditarPerfilForm, CambiarContraseñaForm
from .models import Usuario, Notificacion
from matches.models import Like, Match
from django.db import models


# Vista para manejar el registro de nuevos usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES) # Formulario que incluye campos y archivos
        if form.is_valid():                              # Valida los datos del formulario
            form.save()                                   # Guarda el usuario 
            messages.success(request, '¡Te has registrado correctamente!')                                 
            return redirect('login')                     # Redirige a la página de inicio
        else:
            messages.error(request, 'Hubo un error en el registro. Verifica los datos ingresados.')
    else:
        form = RegistroForm()                            # Si la solicitud es GET, mostrar el formulario vacio
        
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista para manejar la página principal
def home(request):
    return render(request, 'usuarios/home.html')         # Renderiza la plantilla de la pagina principal

def perfil(request):
    return render(request, 'usuarios/perfil.html')


# Vista para editar el perfil del usuario
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado con éxito!')
            return redirect('editar_perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})

# Vista para cambiar la contraseña del usuario
@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = CambiarContraseñaForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Mantener la sesión iniciada después del cambio
            messages.success(request, '¡Contraseña cambiada con éxito!')
            return redirect('editar_perfil')
    else:
        form = CambiarContraseñaForm(user=request.user)
    return render(request, 'usuarios/cambiar_contraseña.html', {'form': form})


@login_required
def historial_actividad(request):
    usuario = request.user  # Obtener el usuario autenticado

    # Obtener likes dados y recibidos
    likes_dados = usuario.likes_dados.all()
    likes_recibidos = usuario.likes_recibidos.all()

    # Obtener matches (donde el usuario es usuario1 o usuario2)
    matches = Match.objects.filter(
        models.Q(usuario1=usuario) | models.Q(usuario2=usuario)
    )

    # Obtener notificaciones no leídas
    notificaciones = usuario.notificaciones.filter(leida=False)

    # Renderizar la plantilla con la información completa del historial de actividad
    return render(request, 'usuarios/historial_actividad.html', {
        'likes_dados': likes_dados,
        'likes_recibidos': likes_recibidos,
        'matches': matches,
        'notificaciones': notificaciones,
    })
