from mainapp.models import Matricula, Notas, Estudiantes, Periodos, Justificaciones
from notas.utils.definitivasCualitativas import isCualitativa
from django.db.models.functions import Cast, Coalesce, Round
from django.contrib.auth.decorators import login_required
from .utils.excel import generarExcel
from django.shortcuts import render
from django.db.models import F, FloatField, DecimalField, Value
# Create your views here.

@login_required
def ver(request):
    if request.method == 'GET':
        matriculas = Matricula.objects.all()
        return render(request, 'ver.html', {
            'matriculas': matriculas
        })
    
@login_required
def secciones(request, id_matricula):
    if request.method == 'GET':
        SECCIONES_POSIBLES = ["A", "B", "C", "D", "E", "F", "G"]
        matricula = Matricula.objects.get(id=id_matricula)
        pensum = matricula.pensum
        secciones = SECCIONES_POSIBLES[:matricula.n_secciones]
        return render(request, 'secciones.html', {
            'matricula': matricula, 
            'secciones': secciones, 
            'pensum': pensum
        })

@login_required
def estudiantes(request):
    if request.method == 'GET':
        matricula_id = request.GET.get('matricula')
        seccion = request.GET.get('seccion')
        matricula = Matricula.objects.get(id=matricula_id)
        estudiantes = Estudiantes.objects.filter(matricula=matricula.id, seccion=seccion)
        return render(request, 'estudiantesVer.html', {
            'matricula': matricula,
            'seccion': seccion,
            'estudiantes': estudiantes
        })

@login_required
def notasVer(request, curso):
    if request.method == 'GET':
        estudiante_id = request.GET.get('estudiante')
        
        # Opcional: Validación de seguridad por si alguien entra a la URL sin el parámetro ?estudiante=
        if not estudiante_id:
            return render(request, 'verNotas.html', {'message': 'No se proporcionó un estudiante válido.'})
            
        estudiante = Estudiantes.objects.get(id=estudiante_id)  
        notas = Notas.objects.filter(estudiante=estudiante.id, materia__curso=curso)
        
        # 1. Creamos la expresión matemática asegurando que los valores por defecto sean flotantes
        promedio_expr = (
            Coalesce(F('notas__primer_momento'), Value(0.0)) + 
            Coalesce(F('notas__segundo_momento'), Value(0.0)) + 
            Coalesce(F('notas__tercer_momento'), Value(0.0))
        ) / Value(3.0)

        # 2. Casteamos a DecimalField ANTES del Round para evitar el Error 500 en PostgreSQL
        justificaciones = Justificaciones.objects.filter(notas__in=notas).annotate(
            definitivaTemplate=Cast(
                Round(
                    Cast(promedio_expr, DecimalField(max_digits=5, decimal_places=2)),
                    2
                ), 
                FloatField()
            )
        )
                
        cursos = Notas.objects.filter(estudiante=estudiante.id).values_list('materia__curso', flat=True).distinct()
        
        isCualitativa(justificaciones, 'definitivaTemplate')
        
        periodos = Periodos.objects.filter(id__in=justificaciones.values('notas__periodos').distinct())
        
        return render(request, 'verNotas.html', {
            'estudiante': estudiante,
            'notas': notas,
            'justificaciones': justificaciones,
            'periodos': periodos,
            'cursos': cursos
        })

@login_required
def descargarExcel(request):
    return generarExcel(request.GET.get('periodo'), request.GET.get('estudiante'))