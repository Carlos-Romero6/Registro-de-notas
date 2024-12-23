from mainapp.models import Notas
from django.http import JsonResponse


def consultarMomento(request):
    materia = request.GET.get('materia')
    estudiante = request.GET.get('estudiante')
    
    try:
        if not materia:
            return JsonResponse({'error' : 'Materia no proporcionada'})
        
        notas = Notas.objects.filter(materia=materia, estudiante=estudiante).first()
        momentos_nulos = []
        if not notas:
            momentos_nulos.append('primer_momento')
            return JsonResponse({'momentos': momentos_nulos})
        momentos_a_verificar = ['segundo_momento', 'tercer_momento','revision']
    
        for momento in momentos_a_verificar:
            valor_del_momento = getattr(notas, momento)
            if valor_del_momento is None:
                momentos_nulos.append(momento)
                
        return JsonResponse({'momentos': momentos_nulos})    

    except:
        return JsonResponse({'error': 'Error inesperado'}, status=404) 