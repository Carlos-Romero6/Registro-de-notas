from mainapp.models import Estudiantes

def obtener(request):
    estudiantes = Estudiantes.objects.filter(seccion=request.GET.get('seccion'), matricula__curso=request.GET.get('curso'))
    return {'curso': request.GET.get('curso'), 'seccion': request.GET.get('seccion'), 'estudiantes': estudiantes}
