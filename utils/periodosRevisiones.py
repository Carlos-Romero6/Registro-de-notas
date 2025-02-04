from mainapp.models import Estudiantes, Notas, Periodos, Materias
from django.http import JsonResponse
from django.forms.models import model_to_dict
def periodoRevisiones(request):
    try:
        estudiante = request.GET.get('estudiante')
        notas_reprobadas= Notas.objects.filter(estudiante=estudiante,estado="REPROBADO").values_list('periodos', flat=True)
        print(notas_reprobadas)
        periodos_reprobados = Periodos.objects.filter(pk__in=notas_reprobadas)
        periodos_list = []
        for periodo_reprobado in periodos_reprobados:
            periodos_list.append(model_to_dict(periodo_reprobado))
        return JsonResponse({'periodos_reprobados': periodos_list})
    except Exception as e:
        print(e)
        return JsonResponse({'Error': 'Error inesperado'})