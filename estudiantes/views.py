from django.shortcuts import render

# Create your views here.

# Menu inicial de la seccion de gestion de estudiantes
def menuEstudiantes(request):
    if request.method == 'GET':
        return render(request, 'menuEstudiantes.html')

def busquedaEstudiantes(request):
    if request.method == 'POST':
        pass
