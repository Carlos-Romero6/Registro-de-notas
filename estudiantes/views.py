from django.shortcuts import render
from utils import buscarEstudiantes, cursosDisponibles
# Create your views here.

# Menu inicial de la seccion de gestion de estudiantes
def menuEstudiantes(request):
    if request.method == 'GET':
        return render(request, 'menuEstudiantes.html', cursosDisponibles.obtener())

def busquedaEstudiantes(request):
    if request.method == 'POST':
        return render(request, 'buscarEstudiantes.html', buscarEstudiantes.obtener(request))
