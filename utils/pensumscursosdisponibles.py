from mainapp.models import Matricula, Pensum
from django.db.models import Count

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

def obtener_pensums():
    """Obtiene los pensums que tienen menos de 5 matrículas asociadas.

    Returns:
        list: Una lista de diccionarios, cada uno representando un pensum con los
            siguientes campos: 'id', 'nombre' y 'num_matriculas'.
    """
    pensums2 = Pensum.objects.annotate(
        num_matriculas=Count('matricula')
    ).filter(num_matriculas__lt=5)
    pensums = [{'id': pensum.id, 'nombre_pensum': pensum.nombre_pensum, 'num_matriculas': pensum.num_matriculas} for pensum in pensums2]
    return {'pensums' : pensums} # Devuelve los pensums obtenidos