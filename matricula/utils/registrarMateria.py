from mainapp.models import Materias, Pensum
from django.http import JsonResponse

def agregar(request):
    if request.method == 'POST':
        try:
            pensum_id = Pensum.objects.get(nombre_pensum = request.POST['pensummateria'])
            nuevaMateria = Materias(
                nombre_materia=request.POST['nombremateria'],
                curso=request.POST['cursomateria'],
                cualitativa=request.POST['cuantitativomateria'],
                pensum = pensum_id
            )
            print(nuevaMateria)
            print(request.POST)
            nuevaMateria.save()
            return JsonResponse({'success': True, 'message': "Registro exitoso."})
        except:
            return JsonResponse({'success': False, 'message': "Datos no validos."})
    return JsonResponse({'success': False, 'message': "Método no permitido."})