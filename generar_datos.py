import os
import django
import random
from faker import Faker

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from mainapp.models import Pensum, Matricula, Estudiantes, Materias, Notas  # Importa tus modelos

# Inicializa Faker
faker = Faker()

# Configuración
CURSOS = [1, 2, 3, 4, 5]
SECCIONES = ['A', 'B', 'C', 'D', 'E']
NUM_PENSUMS = 3
NUM_ESTUDIANTES = 100
NUM_MATERIAS = 10

def crear_pensums():
    print("Creando Pensums...")
    pensums = []
    for _ in range(NUM_PENSUMS):
        nombre_pensum = f"Pensum {faker.word().capitalize()}"
        pensum, created = Pensum.objects.get_or_create(nombre_pensum=nombre_pensum)
        pensums.append(pensum)
    return pensums

def crear_matriculas(pensums):
    print("Creando Matrículas...")
    matriculas = []
    for curso in CURSOS:
        for _ in range(random.randint(3, 5)):  # Entre 3 y 5 matrículas por curso
            matricula = Matricula.objects.create(
                promocion=f"Promoción {faker.year()}",
                curso=curso,
                pensum=random.choice(pensums)
            )
            matriculas.append(matricula)
    return matriculas

def crear_estudiantes(matriculas):
    print("Creando Estudiantes...")
    estudiantes = []
    for _ in range(NUM_ESTUDIANTES):
        matricula = random.choice(matriculas)
        estudiante = Estudiantes.objects.create(
            nombres=faker.first_name(),
            apellidos=faker.last_name(),
            ci=faker.unique.random_number(digits=8),
            genero=random.choice(['M', 'F']),
            seccion=random.choice(SECCIONES),
            estado=random.choice([True, False]),
            flotante=random.choice([True, False]),
            materias_reprobadas=random.randint(0, 3),
            matricula=matricula
        )
        estudiantes.append(estudiante)
    return estudiantes

def crear_materias(pensums):
    print("Creando Materias...")
    materias = []
    for _ in range(NUM_MATERIAS):
        materia = Materias.objects.create(
            nombre_materia=faker.word().capitalize(),
            curso=random.choice(CURSOS),
            cualitativa=random.choice([True, False]),
            pensum=random.choice(pensums)
        )
        materias.append(materia)
    return materias

def crear_notas(estudiantes, materias):
    print("Creando Notas...")
    for estudiante in estudiantes:
        for materia in materias:
            Notas.objects.create(
                primer_momento=random.uniform(0, 20),
                segundo_momento=random.uniform(0, 20),
                tercer_momento=random.uniform(0, 20),
                definitiva=None,  # Se puede calcular posteriormente
                revision=None,
                estado=random.choice(['Aprobado', 'Reprobado']),
                estudiante=estudiante,
                materia=materia
            )

def main():
    print("Generando datos de prueba...")
    
    # Generar datos
    pensums = crear_pensums()
    matriculas = crear_matriculas(pensums)
    estudiantes = crear_estudiantes(matriculas)
    materias = crear_materias(pensums)
    crear_notas(estudiantes, materias)

    print("¡Datos generados exitosamente!")

if __name__ == "__main__":
    main()
