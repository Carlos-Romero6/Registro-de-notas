from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.db.models import F
from mainapp.models import Notas, Justificaciones, Estudiantes, Periodos, Matricula
from .utils.saveDefinitiva import  saveDefinitiva
from .utils.gestionarEstadosAprobadosReprobados import gestionarAprobadosReprobados
from .utils.aprobadosPorRevision import aprobadosPorRevision
from .utils.estudianteRepitiente import estudianteRepitiente
from .utils.estudianteRepitiente import repitienteMateriaCursoAnterior
from decimal import Decimal

# Receptor notas
@receiver(pre_save, sender=Notas)
def gestionNotas(sender, instance,**kwargs):
    print("gestionOk")
    print(instance.__dict__, "1")
    if instance.primer_momento is not None and instance.segundo_momento is not None and instance.tercer_momento is not None:
        print("Ok 3 ✅")
        try:
            if instance.definitiva is not None and instance.definitiva < Decimal(9.50):
                reprobado_previo = True
            else:
                reprobado_previo = False
                
            print(reprobado_previo)
            saveDefinitiva(instance)
            gestionarAprobadosReprobados(instance, reprobado_previo)
            aprobadosPorRevision(instance, reprobado_previo)
            print(instance.estado)
        except Exception as e:
            print(e)
    estudianteRepitiente(instance)


# Receptor períodos
@receiver(pre_save, sender=Periodos)
def gestionPeriodos(sender, instance, **kwargs):
    estudiantes_repitientes = Estudiantes.objects.filter(repitiente=1, estado=1)
    
    for estudiante in estudiantes_repitientes: 
        
        if repitienteMateriaCursoAnterior(estudiante):
            notas_reprobadas_actual = Notas.objects.filter(estudiante=estudiante.id, materia__curso=estudiante.matricula.curso, estado="REPROBADO").count()
            estudiante.materias_reprobadas -= notas_reprobadas_actual
        else: 
            estudiante.materias_reprobadas = 0
        Notas.objects.filter(estudiante=estudiante.id, materia__curso=estudiante.matricula.curso).update(estado="ANULADO")
        estudiante.save()


    for estudiante in estudiantes_repitientes:
        if estudiante.matricula.curso == 1:
            estudiante.flotante = 1

        else: 
            matricula_repetir = Matricula.objects.filter(curso=estudiante.matricula.curso - 1).first()
            estudiante.matricula = matricula_repetir
        estudiante.repitiente = 0
        estudiante.save()
    
    # Gestionar el aumento de los cursos para indicar que ya pasaron el período académico actual
    Matricula.objects.filter(curso__range=(1,5)).update(curso=F('curso') + 1)
'''@receiver(pre_save, sender=Notas)
def saveDefinitiva(sender, instance,**kwargs):
    print("Señal OK")
    if instance.primer_momento and instance.segundo_momento and instance.tercer_momento:  
        print('Creando definitiva')
        instance.definitiva = calcularDefinitiva(instance)

@receiver(pre_save, sender=Notas)
def aprobadosReprobados(sender, instance, **kwargs):
    print("AprobadosReprobados")
    if instance.primer_momento and instance.segundo_momento and instance.tercer_momento and instance.defintiva:
        print("momentos existentes")
        if instance.definitiva < 9.5:
            print("<9.5")
            instance.estado = "APROBADO"
            estudiante = Estudiantes.objects.get(pk=instance.estudiante)
            print("Se encontró al estudiante")
            estudiante.materias_reprobadas += 1'''