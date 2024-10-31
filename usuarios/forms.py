from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Usuario

# Formulario para el registro de usuario
class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'carrera', 'sede', 'genero', 'orientacion', 'intereses', 'bio', 'foto']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@usm.cl'):
            raise forms.ValidationError("El correo debe ser @usm.cl")
        return email

# Formulario para editar el perfil de usuario
class EditarPerfilForm(UserChangeForm):
    password = None  # Excluir el campo de contraseña del formulario de edición general

    class Meta:
        model = Usuario  # Usar el modelo de usuario personalizado
        fields = ['username', 'foto']  # Campos que el usuario puede editar

# Formulario para cambiar la contraseña
class CambiarContraseñaForm(PasswordChangeForm):
    class Meta:
        model = Usuario
        fields = ['old_password', 'new_password1', 'new_password2']
