from django.shortcuts import render, redirect
from usuarios.models import Usuario
from .models import Like
from .models import Grupo
from django.contrib.auth.decorators import login_required

# el @login_required es para que solo usuarios logeados puedan acceder

# Vista para el swiping de perfiles
@login_required
def swiping(request):
    usuario = request.user      # Obtener el usuario actual
                                # Excluir usuarios ya "likados" o a uno mismo
    perfiles = Usuario.objects.exclude(id=usuario.id).exclude(likes_recibidos__usuario_origen=usuario)
    
    if request.method == 'POST':
        usuario_destino_id = request.POST.get('usuario_destino')        # Obtener ID del usuario al que se dio like
        usuario_destino = Usuario.objects.get(id=usuario_destino_id)
        Like.objects.create(usuario_origen=usuario, usuario_destino=usuario_destino) # Crear un nuevo like
        return redirect('swiping')  # Recargar para mostrar el siguiente perfil

    return render(request, 'matches/swiping.html', {'perfiles': perfiles})

# Vista para mostrar los likes dados, recibidos, y los matches
@login_required
def lista_likes(request):
    usuario = request.user                          # Obtener el usuario actual
    likes_dados = usuario.likes_dados.all()         # Obtener los likes dados por el usuario
    likes_recibidos = usuario.likes_recibidos.all() # Obtener los likes recibidos por el usuario
    matches = [like.usuario_destino for like in likes_dados if like.usuario_destino in [l.usuario_origen for l in likes_recibidos]]
    
    return render(request, 'matches/lista_likes.html', {
        'likes_dados': likes_dados,
        'likes_recibidos': likes_recibidos,
        'matches': matches,
    })

# Vista para crear un nuevo grupo
@login_required
def crear_grupo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')           # Obtener el nombre del grupo
        descripcion = request.POST.get('descripcion') # Obtener la descripción del grupo
        grupo = Grupo.objects.create(nombre=nombre, descripcion=descripcion) # Crear el grupo
        grupo.usuarios.add(request.user)              # Añadir el usuario actual al grupo
        return redirect('ver_grupos')                 # Regirigir a la vista de ver grupos

    return render(request, 'matches/crear_grupo.html')

# Vista para listar los grupos
@login_required
def ver_grupos(request):
    grupos = Grupo.objects.all()                      # Obtener todos los grupos
    return render(request, 'matches/ver_grupos.html', {'grupos': grupos})
