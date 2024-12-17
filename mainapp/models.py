from django.db import models
from decimal import Decimal, ROUND_HALF_UP
from django.utils import timezone
# Modelos de las tablas de la base de datos.

class Pensum(models.Model):
    nombre_pensum = models.CharField(max_length=50)

class Matricula(models.Model):
    promocion = models.CharField(max_length=50)
    curso = models.IntegerField(default=1)
    n_secciones = models.IntegerField(default=1)
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)

class Estudiantes(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ci = models.CharField(max_length=8)
    genero = models.CharField(max_length=10, null=True)
    seccion = models.CharField(max_length=1)
    estado = models.BooleanField(default=True)
    flotante = models.BooleanField(default=False)
    materias_reprobadas  = models.IntegerField(default=0)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombres

class Materias(models.Model):
    nombre_materia = models.CharField(max_length=100)
    curso = models.IntegerField()
    cualitativa = models.BooleanField(default=False)
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)

class Periodos(models.Model):
    inicio = models.IntegerField (default=timezone.now().year)
    finalizacion = models.IntegerField(null=True)
class Notas(models.Model):
    primer_momento = models.FloatField(null=True)
    segundo_momento = models.FloatField(null=True)
    tercer_momento = models.FloatField(null=True)
    definitiva = models.FloatField(null=True)
    revision = models.FloatField(null=True)
    estado = models.CharField(max_length=10, null=True)
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE)
    periodos = models.ForeignKey(Periodos, on_delete=models.CASCADE)
    
    # Funcion para calcular definitiva.
    def calcularDefinitiva(self): 
        n_momentos = 3
        definitiva = Decimal((self.primer_momento + self.segundo_momento + self.tercer_momento) / n_momentos).quantize(0, ROUND_HALF_UP)
        return definitiva

class Justificaciones(models.Model):
    primer_momento = models.CharField(max_length=3, null=True)
    segundo_momento = models.CharField(max_length=3, null=True)
    tercer_momento = models.CharField(max_length=3, null=True)
    notas = models.ForeignKey(Notas, on_delete=models.CASCADE)



