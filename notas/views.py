from django.shortcuts import render, get_list_or_404, redirect
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones

# Create your views here.
def notas(request):
    if request.method == 'GET':
        return render(request, 'notas.html')
    
    elif request.method == 'POST':
            ESTUDIANTES = Estudiantes.objects.filter(matricula__curso = request.POST['curso'], seccion=request.POST['seccion'])
            return render(request, 'estudiantes-resultado.html',{
                'estudiantes': ESTUDIANTES
            })
    #  return render(request, 'notas.html')
