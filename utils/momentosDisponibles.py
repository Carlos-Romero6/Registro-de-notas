from mainapp.models import Notas
from django.http import JsonResponse


def consultarMomento(request):

    # Se obtienen los datos enviados por la función de JavaScript en el front
    materia = request.GET.get('materia')
    estudiante = request.GET.get('estudiante')
    
    
    try:
        if not materia:
            return JsonResponse({'error' : 'Materia no proporcionada'})

        # Se obtiene el registro que pertenece a un estudiante y a una materia
        notas = Notas.objects.filter(materia=materia, estudiante=estudiante).first()
        momentos_nulos = []
        if not notas:
            # Si no hay resgistos, se envía el primer momento como nulo
            momentos_nulos.append('primer_momento')
            return JsonResponse({'momentos': momentos_nulos})

            # Se verifica si los momentos de la base de datos son nulos
        momentos_a_verificar = ['segundo_momento', 'tercer_momento','revision']
    
        for momento in momentos_a_verificar:
            valor_del_momento = getattr(notas, momento) # Se accede al valor de un campo del registro
            if valor_del_momento is None:
                momentos_nulos.append(momento) # Si el valor es nulo, se añade a la lista de momentos nulos
                
        return JsonResponse({'momentos': momentos_nulos})    

    except:
        return JsonResponse({'error': 'Error inesperado'}, status=404) 