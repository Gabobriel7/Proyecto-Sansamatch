from django.shortcuts import render, redirect
from usuarios.models import Usuario
from .models import Like
from .models import Grupo
from django.contrib.auth.decorators import login_required

def swiping(request):
    usuario = request.user
    # Excluir usuarios ya "likados" o a uno mismo
    perfiles = Usuario.objects.exclude(id=usuario.id).exclude(likes_recibidos__usuario_origen=usuario)
    
    if request.method == 'POST':
        usuario_destino_id = request.POST.get('usuario_destino')
        usuario_destino = Usuario.objects.get(id=usuario_destino_id)
        Like.objects.create(usuario_origen=usuario, usuario_destino=usuario_destino)
        return redirect('swiping')  # Recargar para mostrar el siguiente perfil

    return render(request, 'matches/swiping.html', {'perfiles': perfiles})

@login_required
def lista_likes(request):
    usuario = request.user
    likes_dados = usuario.likes_dados.all()
    likes_recibidos = usuario.likes_recibidos.all()
    matches = [like.usuario_destino for like in likes_dados if like.usuario_destino in [l.usuario_origen for l in likes_recibidos]]
    
    return render(request, 'matches/lista_likes.html', {
        'likes_dados': likes_dados,
        'likes_recibidos': likes_recibidos,
        'matches': matches,
    })

def crear_grupo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        grupo = Grupo.objects.create(nombre=nombre, descripcion=descripcion)
        grupo.usuarios.add(request.user)
        return redirect('ver_grupos')

    return render(request, 'matches/crear_grupo.html')

def ver_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'matches/ver_grupos.html', {'grupos': grupos})

def swiping(request):
    # Lógica para cargar perfiles
    return render(request, 'matches/swiping.html')