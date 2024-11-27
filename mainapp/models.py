from django.db import models

# Create your models here.

class Pensum(models.Model):
    nombre_pensum = models.CharField(max_length=50)

class Matricula(models.Model):
    promocion = models.CharField(max_length=50)
    curso = models.IntegerField(default=1)
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)

class Estudiantes(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ci = models.CharField(max_length=6)
    seccion = models.CharField(max_length=1)
    estado = models.BooleanField(default=True)
    materias_reprobadas  = models.IntegerField(default=0)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)

class Materias(models.Model):
    nombre_materia = models.CharField(max_length=100)
    curso = models.IntegerField()
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)

class Notas(models.Model):
    primer_lapso = models.FloatField()
    segundo_lapso = models.FloatField()
    tercer_lapso = models.FloatField()
    definitiva = models.FloatField()
    revision = models.FloatField()
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE)

