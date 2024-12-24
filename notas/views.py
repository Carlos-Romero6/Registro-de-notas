from django.shortcuts import render, get_list_or_404, redirect
from django.http import JsonResponse
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones, Periodos
from django.urls import reverse
from utils import cursosDisponibles
# Create your views here.

# Filtrado de estudiantes por curso y sección
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
            
            # Se envían los objetos para mostrar datos en plantillas o enviar en formularios
            'estudiante': estudiante,
            'periodo_actual': periodo_actual,
            'justificaciones': justificaciones,  
            'materias': materias,
            'matricula': matricula
        })
        
        
from django.http import JsonResponse
from mainapp.models import Notas, Justificaciones, Estudiantes, Materias, Periodos

def cargarNota(request):
    print("Cargando nota")
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
                print("Nueva nota creada:", nueva_nota)
            
            # Si la nota ya existe, se actualiza
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
                elif momento == 'revision':
                    nota_existente.revision = nota
                    print(nota_existente.revision)
                nota_existente.save()

            # Se envía un mensaje de éxito si todo se ejecuta según lo esperado
            return JsonResponse({'success': True, 'message': "Nota cargada exitosamente."})
        
    # Se envía un mensaje de error si ocurre un fallo inesperado
    except:
        return JsonResponse({'success': False, 'message': 'Ha ocurrido un fallo inesperado: '})