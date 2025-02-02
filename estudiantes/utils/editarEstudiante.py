from django.contrib.auth.decorators import login_required
from mainapp.models import Estudiantes
from django.http import JsonResponse
from django.db import IntegrityError

# Create your functions here

# Obtiene los datos de un estudiante para ponerlos en un formulario
@login_required
def obtenerDatos(request):
    if request.method == 'GET':
        estudiante = request.GET.get('estudiante')
        estudianteObtenido = Estudiantes.objects.get(id=estudiante)

        return JsonResponse({
            'nombres': estudianteObtenido.nombres,
            'apellidos': estudianteObtenido.apellidos,
            'ci': estudianteObtenido.ci,
            'genero': estudianteObtenido.genero,
            'curso': estudianteObtenido.matricula.curso,
            'seccion': estudianteObtenido.seccion
        })
    
    return JsonResponse({'success': False, 'message': "Método no admitido."})

# Modifica los datos de un estudiante
@login_required
def actualizar(request, estudiante_id):
    if request.method == 'POST':
        # Cuerpo del post
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        ci = request.POST['cedula']
        genero = request.POST['genero']
        seccion = request.POST['seccion']
        try:
            # Ubicar estudiante
            estudiante = Estudiantes.objects.get(id=estudiante_id)

            # Actualizar datos
            estudiante.nombres = nombres
            estudiante.apellidos = apellidos
            estudiante.ci = ci
            estudiante.genero = genero
            estudiante.seccion = seccion

            # Subir actualización
            estudiante.save()
            return JsonResponse({'success': True, 'message': "El estudiante se ha actualizado correctamente."})
        
        # Cedula ya en la base de datos
        except IntegrityError:
            estudianteRegistrado = Estudiantes.objects.get(ci=request.POST['cedula'])
            return JsonResponse({'success': False, 'message': f"El estudiante ya existe. Su cédula ya esta registrada. Corresponde a: {estudianteRegistrado.nombres} {estudianteRegistrado.apellidos}"})
        # Manejo de error
        except:
            return JsonResponse({'success': False, 'message': "Error al actualizar."})
    return JsonResponse({'success': False, 'message': "Método inválido."})