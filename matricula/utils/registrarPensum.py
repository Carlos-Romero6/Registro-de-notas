#Función para agregar el pénsum
from mainapp.models import Pensum
from django.http import JsonResponse

def agregar(request):
    if request.method == 'POST':
        try:
            #Se crea un nuevo objeto a partir de los datos obtenidos en el formulario
            nuevoPensum = Pensum(
                nombre_pensum=request.POST['pensum']
            )
            print(nuevoPensum)
            #Se guarda en la base de datos y se devuelve un mensaje de True o False al Script de acuerdo si se logro o no
            nuevoPensum.save()
            return JsonResponse({'success': True, 'message': "Registro exitoso."})
        except:
            return JsonResponse({'success': False, 'message': "Datos no validos."})
    return JsonResponse({'success': False, 'message': "Método no permitido."})