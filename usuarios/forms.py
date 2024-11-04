from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Usuario

# Formulario para el registro de usuario

class RegistroForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label='Fecha de nacimiento'
    )
    foto = forms.ImageField(required=False, label='Foto de perfil')
    numero_telefono = forms.CharField(max_length=15, required=False, label='Número de Teléfono')
    instagram = forms.CharField(max_length=30, required=False, label='Instagram')
    sede = forms.ChoiceField(choices=Usuario._meta.get_field('sede').choices, label='Sede')
    carrera = forms.ChoiceField(choices=Usuario._meta.get_field('carrera').choices, label='Carrera')
    preferencia = forms.ChoiceField(choices=Usuario._meta.get_field('preferencia').choices, label='Preferencia')
    semestre = forms.ChoiceField(choices=Usuario._meta.get_field('semestre').choices, label='Semestre Actual')
    genero = forms.ChoiceField(choices=Usuario._meta.get_field('genero').choices, label='Género')
    genero_preferido = forms.ChoiceField(choices=Usuario._meta.get_field('genero_preferido').choices, label='¿Qué género quieres ver?')
    

     # Cambiar los campos de selección múltiple a MultipleChoiceField porque me salía un error
   
    # Especificar manualmente las opciones de selección múltiple en el formulario
    sedes_preferidas = forms.MultipleChoiceField(
        choices=[
            ('Casa central', 'Casa central'),
            ('Viña del Mar', 'Viña del Mar'),
            ('Concepción', 'Concepción'),
            ('Vitacura', 'Vitacura'),
            ('San joaquin', 'San joaquin'),
        ],
        widget=forms.CheckboxSelectMultiple,
        label='Sedes preferidas'
    )
    carreras_preferidas = forms.MultipleChoiceField(
        choices=[
            ('Ingeniería Civil', 'Ingeniería Civil'),
            ('I. Civil informatica', 'I. Civil informatica'),
            ('I. Civil Mecánica', 'I. Civil Mecánica'),
        ],
        widget=forms.CheckboxSelectMultiple,
        label='Carreras preferidas'
    )

    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'fecha_nacimiento', 'numero_telefono', 
                  'instagram', 'sede', 'carrera', 'preferencia', 'semestre', 'genero']
        
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
