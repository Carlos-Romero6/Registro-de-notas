from mainapp.models import Notas, Materias, Periodos
from django.http import JsonResponse
from django.forms.models import model_to_dict

def materiasReprobadasRevision(request):
    try:
        estudiante_id = request.GET.get('estudiante')
        print(estudiante_id)
        periodo_id = request.GET.get('periodo')
        print(periodo_id)
        notas_reprobadas = Notas.objects.filter(estudiante=estudiante_id, periodos=periodo_id, estado="REPROBADO").values_list('materia', flat=True)
        print(notas_reprobadas)
        materias = Materias.objects.filter(pk__in=notas_reprobadas)
        print(materias)
        materias_list = []
        for materia in materias:
            materias_list.append(model_to_dict(materia))
            
        return JsonResponse({'materias_reprobadas': materias_list})
    except Exception as e:
        print(e)
        return JsonResponse({'Error': 'Error al cargar las materias'})