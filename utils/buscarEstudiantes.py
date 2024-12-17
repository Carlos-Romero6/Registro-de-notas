from mainapp.models import Estudiantes

def obtener(request):
    try:
        estudiantes = Estudiantes.objects.filter(seccion=request.POST['seccion'], matricula__curso=request.POST['curso'])
        return {'estudiantes': estudiantes}
    except:
        return {'error': "No hay estudiantes en esta seccion"}
