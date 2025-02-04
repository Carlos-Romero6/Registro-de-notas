from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from mainapp.models import Estudiantes
from django.http import JsonResponse

# Recibe el id del estudiante que quiere eliminar y envía una respuesta json en caso de qu elo haya heco exitosamente
@login_required
def porID(request, estudiante_id):
    estudiante = get_object_or_404(Estudiantes, pk=estudiante_id)
    estudiante.estado = False # Cambiar estado de estudiante
    estudiante.save() # Guardar cambios
    
    return JsonResponse({'status': 'success', 'message': f"{estudiante.nombres} {estudiante.apellidos} se ha eliminado"}) # Devuelve un mensaje de exito