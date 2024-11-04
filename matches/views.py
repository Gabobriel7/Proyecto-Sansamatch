from django.shortcuts import render, redirect
from usuarios.models import Usuario
from .models import Like, Match
from .models import Grupo
from django.contrib.auth.decorators import login_required   

# el @login_required es para que solo usuarios logeados puedan acceder

# Vista para el swiping de perfiles
@login_required
def swiping(request):
    if not request.user.is_authenticated: # Verificar si el usuario está autenticado
        return redirect(f'/usuarios/login/?next={request.path}')
    
    usuario = request.user      # Obtener el usuario actual
                                # Excluir usuarios ya "likeados" o a uno mismo
    perfiles = Usuario.objects.exclude(id=usuario.id).exclude(likes_recibidos__usuario_origen=usuario)

    if usuario.genero_preferido != 'Todos': # Para ver el gente del genero que elegiste
        perfiles = perfiles.filter(genero=usuario.genero_preferido)

    if usuario.sedes_preferidas:      # Filtrar según la sede preferida
        perfiles = perfiles.filter(sede__in=usuario.sedes_preferidas)

    if usuario.carreras_preferidas:   # Filtrar según la carrera preferida
        perfiles = perfiles.filter(carrera__in=usuario.carreras_preferidas)

    if usuario.preferencia:           # Filtrar según el tipo de preferencia (amistad, estudio, relación)
        perfiles = perfiles.filter(preferencia=usuario.preferencia)
    
    if request.method == 'POST':
        usuario_destino_id = request.POST.get('usuario_destino')     # Obtener ID del usuario al que se dio like
        usuario_destino = Usuario.objects.get(id=usuario_destino_id)

        # Crear un nuevo like
        like, created = Like.objects.get_or_create(usuario_origen=usuario, usuario_destino=usuario_destino)
        
        # Comprobar si el usuario destino también dio like al usuario actual
        if usuario_destino.likes_dados.filter(usuario_destino=usuario).exists():
            # Si hay like mutuo, crear un Match
            Match.objects.get_or_create(usuario1=min(usuario.id, usuario_destino.id), usuario2=max(usuario.id, usuario_destino.id))

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
