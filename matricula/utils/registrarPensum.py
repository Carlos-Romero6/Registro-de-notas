from mainapp.models import Pensum
from django.http import JsonResponse

def agregar(request):
    if request.method == 'POST':
        try:
            nuevoPensum = Pensum(
                nombre_pensum=request.POST['pensum']
            )
            print(nuevoPensum)
            nuevoPensum.save()
            return JsonResponse({'success': True, 'message': "Registro exitoso."})
        except:
            return JsonResponse({'success': False, 'message': "Datos no validos."})
    return JsonResponse({'success': False, 'message': "Método no permitido."})