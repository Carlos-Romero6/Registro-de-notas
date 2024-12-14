from django.shortcuts import render

# Create your views here.

# Menu inicial de la seccion de gestion de estudiantes
def menuEstudiantes(request):
    return render(request, 'menuEstudiantes.html')
