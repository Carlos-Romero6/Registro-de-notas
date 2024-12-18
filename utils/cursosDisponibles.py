from mainapp.models import Matricula

# Obtiene las secciones disponibles
def obtener():
	# Constante con una tupla con cada uno de los nombres de los cursos
    CURSOS_EXISTENTES = ("1er año", "2do año", "3er año", "4to año", "5to año")
    # Función lambda para devolver el nombre del año en base al ID
    numeroCurso = lambda indice: CURSOS_EXISTENTES[indice]
    # Consulta cursos de las matriculas dentro del rango (1,5)
    cursosDisponibles = set(Matricula.objects.filter(curso__range=(1,5)).values_list('curso', flat=True))

    # Devolvera un diccionario con los cursos existentes
    cursos = [ {"id": iterable + 1, "nombre": numeroCurso(iterable), "habilitado": (iterable + 1) in cursosDisponibles} for iterable in range(5)]

    return {'cursos' : cursos} # Devuelve los cursos obtenidos

"""    for iterable in range(5):
        curso = {
            "id": iterable + 1,
            "nombre": numeroCurso(iterable),
            "habilitado": (iterable + 1) in cursosDisponibles
        }
        cursos.append(curso) """