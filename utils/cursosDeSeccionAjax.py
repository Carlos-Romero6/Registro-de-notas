from django.http import JsonResponse
from mainapp.models import Matricula

def consultarSecciones(request):
    curso = request.GET.get('curso') # Se obtiene el curso elegido en el selector desde el frontend
    if not curso:
        return JsonResponse({'error' : 'Curso no proporcionado'})

    POSIBLES_SECCIONES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    try:
        # Obtener la matricula para el curso proporcionado
        matricula = Matricula.objects.get(curso=curso)

        # Obtener el numero de secciones para ese campo
        N_SECCIONES = matricula.n_secciones

        # Crear lista con secciones disponibles
        SECCIONES_DISPONIBLES = POSIBLES_SECCIONES[:N_SECCIONES]
        return JsonResponse({'secciones' : SECCIONES_DISPONIBLES})
    except:
        return JsonResponse({'error': 'Curso no encontrado'}, status=404)
