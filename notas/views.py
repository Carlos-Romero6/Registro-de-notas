from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones, Periodos
from utils import cursosDisponibles
# Create your views here.
def notas(request):
    if request.method == 'GET':
        return render(request, 'menuNotas.html',cursosDisponibles.obtener())
    
    elif request.method == 'POST':
                
                ESTUDIANTES = Estudiantes.objects.filter(matricula__curso = request.POST['curso'], seccion=request.POST['seccion'], estado=True)
                return render(request, 'estudiantes-resultado.html',{
                'estudiantes': ESTUDIANTES,
                'curso': request.POST['curso'],
                'seccion': request.POST['seccion'],
            })



def notasEstudiante(request, id_estudiante):
    if request.method == 'GET':
        estudiante = Estudiantes.objects.get(pk=id_estudiante)
        matricula = Matricula.objects.get(pk=estudiante.matricula_id)
        curso = matricula.curso
        pensum = matricula.pensum
        notas = Notas.objects.filter(estudiante=id_estudiante, materia__pensum=pensum, materia__curso=curso)
        justificaciones = Justificaciones.objects.filter(notas__in=notas)
        periodo_actual = Periodos.objects.latest('id')
        return render(request, 'notas-estudiante.html', {
            'estudiante': estudiante,
            'periodo_actual': periodo_actual,
            'justificaciones': justificaciones
        })