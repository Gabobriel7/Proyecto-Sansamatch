from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'carrera', 'sede', 'genero', 'orientacion', 'intereses', 'bio', 'foto']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@usm.cl'):
            raise forms.ValidationError("El correo debe ser @usm.cl")
        return email