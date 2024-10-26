from django.shortcuts import render, redirect
from .forms import RegistroForm

# Vista para manejar el registro de nuevos usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES) # Formulario que incluye campos y archivos
        if form.is_valid():                              # Valida los datos del formulario
            form.save()                                  # Guarda el usuario 
            return redirect('login')                     # Redirige a la página de inicio
    else:
        form = RegistroForm()                            # Si la solicitud es GET, mostrar el formulario vacio
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista para manejar la página principal
def home(request):
    return render(request, 'usuarios/home.html')         # Renderiza la plantilla de la pagina principal
