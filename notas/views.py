from django.shortcuts import render, get_list_or_404, redirect
from django.http import JsonResponse
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones, Periodos
from django.urls import reverse
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
        materias = Materias.objects.filter(pensum=pensum, curso=curso)
        notas = Notas.objects.filter(estudiante=id_estudiante, materia__pensum=pensum, materia__curso=curso)
        justificaciones = Justificaciones.objects.filter(notas__in=notas)
        periodo_actual = Periodos.objects.latest('id')
        return render(request, 'notas-estudiante.html', {
            'estudiante': estudiante,
            'periodo_actual': periodo_actual,
            'justificaciones': justificaciones,
            'materias': materias,
        })
        
        
def cargarNota(request):
    if request.method == 'POST':
        periodo = request.POST['periodo']
        materia = request.POST['materia']
        estudiante = request.POST['estudiante']
        momento = request.POST['momento']
        nota = request.POST['nota']
        justificacion = request.POST['justificacion']
        
        if momento == 'primer_momento':
            nueva_nota = Notas(estudiante=estudiante, materia=materia, periodo=periodo, primer_momento=nota)
            nueva_nota.save()
            nueva_justificacion = Justificaciones(notas=nueva_nota, primer_momento=justificacion)
            nueva_justificacion.save()
            print(nueva_nota)
        else:
            nota_existente = Notas.objects.get(estudiante=estudiante, materia=materia, periodo=periodo)
            justificacion_cargar = Justificaciones.objects.get(notas=nota_existente)
            if momento == 'segundo_momento':
                nota_existente.segundo_momento = nota
                justificacion_cargar.segundo_momento = justificacion
                justificacion_cargar.save()
            elif momento == 'tercer_momento':
                nota_existente.tercer_momento = nota
                justificacion_cargar.tercer_momento = justificacion
                justificacion_cargar.save()
            elif momento == 'revision':
                nota_existente.revision = nota
            nota_existente.save()
            return JsonResponse({'success': True, 'message': "Nota cargada exitosamente."})