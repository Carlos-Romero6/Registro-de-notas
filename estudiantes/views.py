from django.contrib.auth.decorators import login_required
from utils import buscarEstudiantes, cursosDisponibles
from django.shortcuts import render
# Create your views here.

# Menu inicial de la seccion de gestion de estudiantes
@login_required
def menuEstudiantes(request):
    if request.method == 'GET':
        return render(request, 'menuEstudiantes.html', cursosDisponibles.obtener())

@login_required
def busquedaEstudiantes(request):
    if request.method == 'GET':
        return render(request, 'buscarEstudiantes.html', buscarEstudiantes.obtener(request))
