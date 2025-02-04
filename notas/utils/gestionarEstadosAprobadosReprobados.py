from mainapp.models import Estudiantes
from django.db.models import F
from decimal import Decimal

def gestionarAprobadosReprobados(instance, reprobado_previo):
    print("gestionar")
    print(instance.__dict__, "2")
    print(getattr(instance, 'definitiva'))
    print(reprobado_previo)
    if instance.definitiva is not None:
        try:
            if getattr(instance, 'definitiva') <  Decimal(9.50):
                print("funciona")
                if not reprobado_previo:
                    instance.estado = "REPROBADO"
                    estudiante = Estudiantes.objects.filter(pk=instance.estudiante_id).update(materias_reprobadas=F('materias_reprobadas') + 1 ) 
            else:
                instance.estado = "APROBADO"
                if reprobado_previo:
                    estudiante = Estudiantes.objects.filter(pk=instance.estudiante_id).update(materias_reprobadas=F('materias_reprobadas') - 1 ) 
        except Exception as e:  
            print(e)

