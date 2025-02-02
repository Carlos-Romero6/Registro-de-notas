from django.contrib.auth.decorators import login_required
from mainapp.models import Estudiantes, Matricula
from django.http import JsonResponse
from django.db import IntegrityError

# Logica para añadir un estudiante a la tabla de estudiantes
@login_required
def agregar(request):
    if request.method == 'POST':
        try:
            matricula_id = Matricula.objects.get(curso=request.POST['curso'])
            nuevoEstudiante = Estudiantes(
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                ci=request.POST['cedula'],
                genero=request.POST['genero'],
                matricula=matricula_id,
                seccion=request.POST['seccion']
            )
            print(nuevoEstudiante)
            nuevoEstudiante.save()

        # En caso de que la cedula ya esté registrada en la base de datos
        except IntegrityError:
            estudianteRegistrado = Estudiantes.objects.get(ci=request.POST['cedula'])
            if not estudianteRegistrado.estado:
                return JsonResponse({'success': False, 'exist': True, 'message': f"La cédula del estudiante corresponde a un estudiante que estudió en la institución. Se llama: {estudianteRegistrado.nombres} {estudianteRegistrado.apellidos}. ¿Desea reintegrarlo?"})
            
            return JsonResponse({'success': False, 'message': f"La cedula del estudiante ya esta registrada. Pertenece a: {estudianteRegistrado.nombres} {estudianteRegistrado.apellidos}"})
        
        # Manejo de error
        except:
            return JsonResponse({'success': False, 'message': "Datos no validos."})
    return JsonResponse({'success': False, 'message': "Método no permitido."})

# Reintegrar un estudiante que ha sido eliminado
@login_required
def reintegrarEstudiante(request):
    estudiante = Estudiantes.objects.get(pk=request.GET.get('estudiante'))
    if estudiante is None:
        return JsonResponse({'success': False, 'message': "El estudiante no existe"})
    if estudiante.estado:
        return JsonResponse({'success': False, 'message': "El estudiante ya está activo"})
    
    # Cambiar datos
    estudiante.estado = True
    estudiante.matricula = request.GET.get('matricula')
    estudiante.seccion = request.GET.get('seccion')
    estudiante.save()
    
    return JsonResponse({'success': False, 'message': "El estudiante ha sido reintegrado exitosamente."})
