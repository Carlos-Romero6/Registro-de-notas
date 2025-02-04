from mainapp.models import Notas
from decimal import Decimal, ROUND_HALF_UP
def calcularDefinitiva(instance, *args, **kwargs):
    print('Calculando definitiva')
    primer_momento = instance.primer_momento
    segundo_momento = instance.segundo_momento
    tercer_momento = instance.tercer_momento
    print(primer_momento, segundo_momento, tercer_momento)
    NOTAS = [primer_momento, segundo_momento, tercer_momento]
    definitiva = 0
    definitiva = Decimal(sum(float(nota) for nota in NOTAS if nota is not None) / len(NOTAS))
    definitiva = definitiva.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    print(definitiva)
    
    return definitiva