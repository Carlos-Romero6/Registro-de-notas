from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones, Periodos
from utils import cursosDisponibles
from django.db.models import F, FloatField, DecimalField
from django.db.models.functions import Cast, Coalesce, Round
from .utils.definitivasCualitativas import isCualitativa
from .utils.estudianteRepitiente import estudianteRepitiente

# Create your views here.
# Filtrado de estudiantes por curso y sección
@login_required
def notas(request):
    if request.method == 'GET':
        usuario = request.user
        return render(request, 'menuNotas.html', cursosDisponibles.obtener())
    
    elif request.method == 'POST':
        ESTUDIANTES = Estudiantes.objects.filter(
            matricula__curso=request.POST.get('curso'), 
            seccion=request.POST.get('seccion'), 
            estado=1, 
            flotante=0
        )
        return render(request, 'estudiantes-resultado.html', {
            'estudiantes': ESTUDIANTES,
            'curso': request.POST.get('curso'),
            'seccion': request.POST.get('seccion')
        })

# Filtrado de notas de un estudiante en cada materia con sus respectivas justificaciones
@login_required
def notasEstudiante(request, id_estudiante):
    if request.method == 'GET':
        if Periodos.objects.exists():
            usuario = request.user
            
            estudiante = get_object_or_404(Estudiantes, pk=id_estudiante, estado=1)
            
            try:
                matricula = Matricula.objects.get(pk=estudiante.matricula_id)
            except Matricula.DoesNotExist:
                return render(request, 'notas-estudiante.html', {
                    'message': 'Este estudiante no posee una matrícula asignada actualmente.'
                })
            
            curso = matricula.curso
            pensum = matricula.pensum
            materias = Materias.objects.filter(pensum=pensum, curso=curso)
            periodo_actual = Periodos.objects.latest('id')
            
            notas = Notas.objects.filter(
                estudiante=id_estudiante, 
                materia__pensum=pensum, 
                materia__curso=curso, 
                periodos=periodo_actual
            )
            
            # Expresión del promedio sumando momentos
            promedio_expr = (
                Coalesce(F('notas__primer_momento'), 0.0) + 
                Coalesce(F('notas__segundo_momento'), 0.0) + 
                Coalesce(F('notas__tercer_momento'), 0.0)
            ) / 3.0

            # 2. Corrección para PostgreSQL: Se castea a DecimalField antes de aplicar Round
            justificaciones = Justificaciones.objects.filter(notas__in=notas).annotate(
                definitivaTemplate=Cast(
                    Round(
                        Cast(promedio_expr, DecimalField(max_digits=5, decimal_places=2)), 
                        2
                    ), 
                    FloatField()
                )
            )
            
            isCualitativa(justificaciones, 'definitivaTemplate')

            return render(request, 'notas-estudiante.html', {
                'usuario': usuario,
                'estudiante': estudiante,
                'periodo_actual': periodo_actual,
                'justificaciones': justificaciones,  
                'materias': materias,
                'matricula': matricula,
            })
        else:
            return render(request, 'notas-estudiante.html', {
                'message': 'No hay periodos activos, cree su primer período académico y vuelva a intentarlo.'
            })

# Carga de notas y justificaciones en la base de datos
def cargarNota(request):
    try:
        if request.method == 'POST':
            periodo_id = request.POST.get('periodo')
            materia_id = request.POST.get('materia')
            estudiante_id = request.POST.get('estudiante')
            momento = request.POST.get('momento')
            nota = float(request.POST.get('nota'))
            justificacion = request.POST.get('justificacion')
            
            estudiante = Estudiantes.objects.get(pk=estudiante_id)
            periodo = Periodos.objects.get(pk=periodo_id)
            materia = Materias.objects.get(pk=materia_id)
            
            if momento == 'primer_momento' and not Notas.objects.filter(estudiante=estudiante, materia=materia, periodos=periodo).exists():
                nueva_nota = Notas(estudiante=estudiante, materia=materia, periodos=periodo, primer_momento=nota)
                nueva_nota.save()
                nueva_justificacion = Justificaciones(notas=nueva_nota, primer_momento=justificacion)
                nueva_justificacion.save()
            else:
                nota_existente = Notas.objects.get(estudiante=estudiante, materia=materia, periodos=periodo)
                justificacion_cargar = Justificaciones.objects.get(notas=nota_existente.id)
                
                if momento == 'segundo_momento':
                    nota_existente.segundo_momento = nota
                    justificacion_cargar.segundo_momento = justificacion
                    justificacion_cargar.save()
                elif momento == 'tercer_momento':
                    nota_existente.tercer_momento = nota
                    justificacion_cargar.tercer_momento = justificacion
                    justificacion_cargar.save()
                nota_existente.save()

            return JsonResponse({'success': True, 'message': "Nota cargada exitosamente."})
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Ha ocurrido un fallo inesperado: {str(e)}'})

def modificarNota(request):
    try:
        if request.method == 'POST':
            periodo_id = request.POST.get('periodo_modificar')
            estudiante_id = request.POST.get('estudiante_modificar')
            notas_id = request.POST.get('notas_modificar')
            materia_id = request.POST.get('materia_modificar')
            justificacion_primer_momento = request.POST.get('justificacion_primer_momento_modificar')
            justificacion_segundo_momento = request.POST.get('justificacion_segundo_momento_modificar')            
            justificacion_tercer_momento = request.POST.get('justificacion_tercer_momento_modificar')
            primer_momento = request.POST.get('primer_momento_modificar')
            segundo_momento = request.POST.get('segundo_momento_modificar')
            tercer_momento = request.POST.get('tercer_momento_modificar')

            materia = Materias.objects.get(pk=materia_id)
            periodo = Periodos.objects.get(pk=periodo_id)
            estudiante = Estudiantes.objects.get(pk=estudiante_id)
            notas = Notas.objects.get(pk=notas_id, estudiante=estudiante, periodos=periodo, materia=materia)
            justificacion = Justificaciones.objects.get(notas=notas.id)
            
            if notas.primer_momento is not None and justificacion.primer_momento is not None:
                notas.primer_momento = primer_momento 
                justificacion.primer_momento = justificacion_primer_momento
            
            if notas.segundo_momento is not None and justificacion.segundo_momento is not None:
                notas.segundo_momento = segundo_momento
                justificacion.segundo_momento = justificacion_segundo_momento
            
            if notas.tercer_momento is not None and justificacion.tercer_momento is not None:
                notas.tercer_momento = tercer_momento
                justificacion.tercer_momento = justificacion_tercer_momento
                
            justificacion.save()
            notas.save()         
        
        return JsonResponse({'success': True, 'message': "Nota modificada exitosamente."})
    
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Ha ocurrido un fallo inesperado: {str(e)}'})

def cargarRevisiones(request):
    try:
        if request.method == 'POST':
            periodo = request.POST.get('periodoRevision')
            materia = request.POST.get('materiaRevision')
            estudiante = request.GET.get('estudiante')
            revision = request.POST.get('cargarRevision')

            periodo_id = Periodos.objects.get(pk=periodo)
            materia_id = Materias.objects.get(pk=materia)
            estudiante_id = Estudiantes.objects.get(pk=estudiante)
            
            notas_existentes = Notas.objects.get(periodos=periodo_id.id, materia=materia_id.id, estudiante=estudiante_id.id)

            if notas_existentes.revision is None:
                if Decimal(revision) < Decimal("9.50"):
                    return JsonResponse({'success': False, 'message': "La revisión que ha proporcionado no es válida. Ingrese una revisión que permita aprobar la materia."})
                else:
                    notas_existentes.revision = revision
                    notas_existentes.save()
                    estudianteRepitiente(notas_existentes)
                    return JsonResponse({'success': True, 'message': "La revisión ha sido cargada exitosamente."})
            else:
                return JsonResponse({'success': True, 'message': "La revisión ya fue cargada previamente."})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error inesperado: {str(e)}'})

def culminarPeriodo(request):
    if request.method == 'POST':
        try:
            if Matricula.objects.filter(curso=1).exists():
                if Periodos.objects.exists():
                    ultimo_periodo = Periodos.objects.latest('id')
                    inicio = int(ultimo_periodo.finalizacion)
                    nuevo_periodo = Periodos(inicio=inicio, finalizacion=inicio + 1)
                    nuevo_periodo.save()
                    return JsonResponse({'success': True, 'message': 'El período se ha culminado y se ha iniciado uno nuevo exitosamente.'})

                elif Matricula.objects.exists():
                    ultima_matricula = Matricula.objects.latest('id')
                    inicio = int(ultima_matricula.promocion)
                    nuevo_periodo = Periodos(inicio=inicio, finalizacion=inicio + 1)
                    nuevo_periodo.save()
                    return JsonResponse({'success': True, 'message': 'El período se ha culminado y se ha iniciado uno nuevo exitosamente'})

                else:
                    return JsonResponse({'success': False, 'message': 'No se ha encontrado una matrícula, por favor carga una matrícula e inténtelo de nuevo.'})
            else:
                return JsonResponse({'message': 'No se ha encontrado una matrícula correspondiente al primer año, por favor cargue una e intente de nuevo.'}) 
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})