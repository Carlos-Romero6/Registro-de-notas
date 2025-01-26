from mainapp.models import Estudiantes, Materias, Matricula, Notas

def repetienteNumMateriasReprobadas (instance):
    estudiante = Estudiantes.objects.get(pk=instance.estudiante.id)
    print(estudiante.__dict__)
    return estudiante.materias_reprobadas > 2


def repitienteMateriaCursoAnterior(instance):
    if isinstance(instance, Estudiantes):
        print("Curso Anterior Estudiante")
        estudiante_id = instance.id
        estudiante_curso = instance.matricula.curso
    else:
        print("Curso Anterior")
        estudiante_id = instance.estudiante.id
        estudiante_curso = instance.estudiante.matricula.curso
        print(estudiante_curso)

    return Notas.objects.filter(estudiante=estudiante_id, estado="REPROBADO", materia__curso__lt=estudiante_curso).exists()


def estudianteRepitiente(instance):
    try:
        estudiante = Estudiantes.objects.get(pk=instance.estudiante.id)
        if repetienteNumMateriasReprobadas(instance) or repitienteMateriaCursoAnterior(instance):
            print(repetienteNumMateriasReprobadas(instance), repitienteMateriaCursoAnterior(instance))
            estudiante.repitiente = 1
        else:
            print("No mas repitiente")
            estudiante.repitiente = 0
        print(estudiante.__dict__)
        estudiante.save()
    except Exception as e:
        print(e)