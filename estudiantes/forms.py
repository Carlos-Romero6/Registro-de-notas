from mainapp.models import Estudiantes
from django import forms

class FormularioEstudiante(forms.Form):
    nombres = forms.CharField(
        label="Nombres:",
        max_length=60,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe los nombres del estudiante',
        })
    )
    apellidos = forms.CharField(
        label="Apellidos:",
        max_length=60,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe los apellidos del estudiante',
        })
    )
    ci = forms.CharField(
        label="Cedula de identidad:",
        max_length=10,
        required=True,
        widget=forms.CharField(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe la cedula de identidad del estudiante',
        })
    )

    GENEROS=[('Masculino','Masculino'),('Femenino','Femenino')]
    genero = forms.ChoiceField(
        label="Género:",
        required=True,
        choices=GENEROS,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
