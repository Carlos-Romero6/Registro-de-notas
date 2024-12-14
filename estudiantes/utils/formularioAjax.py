from django.http import JsonResponse
from mainapp.models import Estudiantes

def consultarSecciones(request):
    if request.method == 'GET':
        curso = request.GET.get('curso')
        secciones = Estudiantes.objects.filter(matricula__curso=curso).values_list('seccion', flat=True).distinct()
        secciones = list(secciones)
        return JsonResponse({'secciones' : secciones})
