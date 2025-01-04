from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from mainapp.models import Notas, Justificaciones
from .utils.calculoDefinitiva import calcularDefinitiva

@receiver(pre_save, sender=Notas)
def saveDefinitiva(sender, instance,**kwargs):
    print("Señal OK")
    if instance.primer_momento and instance.segundo_momento and instance.tercer_momento:  
        print('Creando definitiva')
        instance.definitiva = calcularDefinitiva(instance)
        