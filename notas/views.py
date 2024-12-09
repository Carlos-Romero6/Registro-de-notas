from django.shortcuts import render
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones

# Create your views here.
def notas(request):
    if request.method == 'GET':
        pass