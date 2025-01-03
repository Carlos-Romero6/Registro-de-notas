from mainapp.models import Matricula, Pensum
from django.http import JsonResponse

def agregar(request):
    if request.method == 'POST':
        try:
            pensum_id = Pensum.objects.get(pk = request.POST['pensumid'])
            nuevaMatricula = Matricula(
                promocion=request.POST['promocion'],
                curso=request.POST['curso'],
                n_secciones=request.POST['secciones'],
                pensum=pensum_id
            )
            print(nuevaMatricula)
            print(request.POST)
            nuevaMatricula.save()
            return JsonResponse({'success': True, 'message': "Registro exitoso."})
        except:
            return JsonResponse({'success': False, 'message': "Datos no validos."})
    return JsonResponse({'success': False, 'message': "Método no permitido."})