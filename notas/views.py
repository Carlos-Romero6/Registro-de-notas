from django.shortcuts import render, get_list_or_404, redirect
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones

# Create your views here.
def notas(request):
    if request.method == 'GET':
        return render(request, 'notas.html')
    
    elif request.method == 'POST':
            tblestudiantes_curso_seccion = Estudiantes.get_list_or_404(curso=request.POST['curso'], seccion = request.POST['seccion'])
            return render(request, 'estudiantes-resultado.html',{
                'tblestudiantes': tblestudiantes_curso_seccion
            })
    #  return render(request, 'notas.html')
