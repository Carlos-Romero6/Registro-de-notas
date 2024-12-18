from mainapp.models import Estudiantes, Matricula
from django.http import JsonResponse

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
            return JsonResponse({'success': True, 'message': "Registro exitoso."})
        except:
            return JsonResponse({'success': False, 'message': "Datos no validos."})
    return JsonResponse({'success': False, 'message': "Método no permitido."})