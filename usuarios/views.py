from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages

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