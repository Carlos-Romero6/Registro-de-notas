from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from mainapp.models import Notas, Justificaciones, Estudiantes
from .utils.saveDefinitiva import  saveDefinitiva
from .utils.gestionarEstadosAprobadosReprobados import gestionarAprobadosReprobados
from decimal import Decimal

@receiver(pre_save, sender=Notas)
def gestionNotas(sender, instance,**kwargs):
    print("gestionOk")
    print(instance.__dict__)
    if instance.primer_momento is not None and instance.segundo_momento is not None and instance.tercer_momento is not None:
        print("gestion")
        try:
            if instance.definitiva is not None and instance.definitiva < Decimal(9.50):
                reprobado_previo = True
            else:
                reprobado_previo = False
            print(reprobado_previo)
            saveDefinitiva(instance)
            gestionarAprobadosReprobados(instance, reprobado_previo)
            print(instance.estado)
        except Exception as e:
            print(e)

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