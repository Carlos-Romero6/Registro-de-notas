from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones, Periodos
from utils import cursosDisponibles
from django.db.models import F, FloatField
from django.db.models.functions import Cast, Coalesce, Round
from .utils.definitivasCualitativas import isCualitativa
# Create your views here.

# Filtrado de estudiantes por curso y sección
@login_required
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

# Filtrado de notas de un estudiante en cada materia con sus respectivas justificaciones
@login_required
def notasEstudiante(request, id_estudiante):

    if request.method == 'GET':
        usuario = request.user
        estudiante = Estudiantes.objects.get(pk=id_estudiante, estado=1)
        matricula = Matricula.objects.get(pk=estudiante.matricula_id)
        curso = matricula.curso
        pensum = matricula.pensum
        materias = Materias.objects.filter(pensum=pensum, curso=curso)
        notas = Notas.objects.filter(estudiante=id_estudiante, materia__pensum=pensum, materia__curso=curso)
        justificaciones = Justificaciones.objects.filter(notas__in=notas).annotate(
            definitivaTemplate=Cast(
                Round((Coalesce(F('notas__primer_momento'), 0) + Coalesce(F('notas__segundo_momento'), 0) + Coalesce(F('notas__tercer_momento'), 0)) / 3, 2), FloatField()
                )
            )
        isCualitativa(justificaciones, 'definitivaTemplate')
        periodo_actual = Periodos.objects.latest('id')

        return render(request, 'notas-estudiante.html', {
            
            # Se envían los objetos para mostrar datos en plantillas o enviar en formularios
            'usuario': usuario,
            'estudiante': estudiante,
            'periodo_actual': periodo_actual,
            'justificaciones': justificaciones,  
            'materias': materias,
            'matricula': matricula,
        })


def cargarNota(request):
    
    try:
        if request.method == 'POST':
        
        # Se obtienen los datos enviados por el formulario
            periodo_id = request.POST.get('periodo')
            materia_id = request.POST.get('materia')
            estudiante_id = request.POST.get('estudiante')
            momento = request.POST.get('momento')
            nota = request.POST.get('nota')
            justificacion = request.POST.get('justificacion')
            
            # Se obtienen los objetos de la base de datos según lo enviado en el formulario
            estudiante = Estudiantes.objects.get(pk=estudiante_id)
            periodo = Periodos.objects.get(pk=periodo_id)
            materia = Materias.objects.get(pk=materia_id)

            # Conversion de la nota enviada a float
            nota = float(nota)
            
            # Se verifica si la nota ya existe en la base de datos
            if momento == 'primer_momento':
                nueva_nota = Notas(estudiante=estudiante, materia=materia, periodos=periodo, primer_momento=nota)
                nueva_nota.save()
                nueva_justificacion = Justificaciones(notas=nueva_nota, primer_momento=justificacion)
                nueva_justificacion.save()
                
            
            # Si la nota ya existe, se actualiza
            else:
                print("else")
                print(periodo)
                nota_existente = Notas.objects.get(estudiante=estudiante, materia=materia, periodos=periodo)
                print("else2")
                justificacion_cargar = Justificaciones.objects.get(notas=nota_existente.id)
                print("else2")
                if momento == 'segundo_momento':
                    nota_existente.segundo_momento = nota
                    justificacion_cargar.segundo_momento = justificacion
                    justificacion_cargar.save()
                elif momento == 'tercer_momento':
                    nota_existente.tercer_momento = nota
                    justificacion_cargar.tercer_momento = justificacion
                    justificacion_cargar.save()
                """elif momento == 'revision':
                    nota_existente.revision = nota
                    print(nota_existente.revision)
                nota_existente.save()"""

            # Se envía un mensaje de éxito si todo se ejecuta según lo esperado
            return JsonResponse({'success': True, 'message': "Nota cargada exitosamente."})
        
    # Se envía un mensaje de error si ocurre un fallo inesperado
    except:
        return JsonResponse({'success': False, 'message': 'Ha ocurrido un fallo inesperado: '})
    
def modificarNota(request):
    try:
        if request.method == 'POST':
            
            # Obtención de los datos ingresados en el formulario
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
            revision = request.POST.get('revision_modificar')

            # Dterminación del registro de las notas y justificaciones que cumplen con la materia, el periodo y el estudiante en cuestión
            materia = Materias.objects.get(pk=materia_id)
            periodo = Periodos.objects.get(pk=periodo_id)
            estudiante = Estudiantes.objects.get(pk=estudiante_id)
            notas = Notas.objects.get(pk=notas_id, estudiante=estudiante, periodos=periodo, materia=materia)
            justificacion = Justificaciones.objects.get(notas=notas.id)
            
            
            # Modificación de las notas y justificaciones según lo ingresado por el usuario
            if notas.primer_momento and justificacion.primer_momento:
                notas.primer_momento = primer_momento 
                justificacion.primer_momento = justificacion_primer_momento
            
            if notas.segundo_momento and justificacion.segundo_momento:
                notas.segundo_momento = segundo_momento
                justificacion.segundo_momento = justificacion_segundo_momento
            
            if notas.tercer_momento and justificacion.tercer_momento:
                notas.tercer_momento = tercer_momento
                justificacion.tercer_momento = justificacion_tercer_momento
            
            if notas.revision:
                notas.revision = revision
                
            # Guardado de lo modificado en la base de datos
            
            justificacion.save()
            notas.save()         
        
        return JsonResponse({'success': True, 'message': "Nota modificada exitosamente."})
    
    except:
        return JsonResponse({'success': False, 'message': 'Ha ocurrido un fallo inesperado'})


