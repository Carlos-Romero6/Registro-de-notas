from mainapp.models import Notas, Estudiantes
from django.db.models import F


def aprobadosPorRevision(instance, reprobado_previo):
    if instance.revision is not None and reprobado_previo:
        instance.estado = "APROBADO"
        estudiante = Estudiantes.objects.filter(pk=instance.estudiante_id).update(materias_reprobadas=F('materias_reprobadas') - 1)