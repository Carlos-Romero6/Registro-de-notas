from mainapp.models import Estudiantes
from django.db.models import F
from decimal import Decimal

def gestionarAprobadosReprobados(instance, reprobado_previo):
    print("gestionar")
    print(instance.__dict__)
    print(getattr(instance, 'definitiva'))
    print(reprobado_previo)
    if instance.definitiva is not None and not reprobado_previo:
        try:
            if getattr(instance, 'definitiva') <  Decimal(9.50):
                print("funciona")
                instance.estado = "REPROBADO"
                print(instance.estado)
                estudiante = Estudiantes.objects.filter(pk=instance.estudiante_id).update(materias_reprobadas=F('materias_reprobadas') + 1 )
                print(estudiante.__dict__)
            else:
                instance.estado = "APROBADO"
                print(instance.estado)
        except Exception as e:  
            print(e)

