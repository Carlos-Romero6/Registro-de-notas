#Función para agregar la matricula
from mainapp.models import Matricula, Pensum
from django.http import JsonResponse

def agregar(request):
    if request.method == 'POST':
        try:
            #Se crea una variable con el objeto del pensum al que se le desea añadir a la matricula
            pensum_id = Pensum.objects.get(pk = request.POST['pensumid'])
            #Se crea un nuevo objeto a partir de los datos obtenidos en el formulario
            nuevaMatricula = Matricula(
                promocion=request.POST['promocion'],
                curso=request.POST['curso'],
                n_secciones=request.POST['secciones'],
                pensum=pensum_id
            )
            print(nuevaMatricula)
            print(request.POST)
            #Se guarda en la base de datos y se devuelve un mensaje de True o False al Script de acuerdo si se logro o no
            nuevaMatricula.save()
            return JsonResponse({'success': True, 'message': "Registro exitoso."})
        except:
            return JsonResponse({'success': False, 'message': "Datos no validos."})
    return JsonResponse({'success': False, 'message': "Método no permitido."})