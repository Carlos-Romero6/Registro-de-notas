from mainapp.models import Estudiantes, Periodos, Notas, Justificaciones
from notas.utils.definitivasCualitativas import isCualitativa
from django.db.models.functions import Cast, Coalesce, Round
from django.db.models import F, FloatField
from django.http import HttpResponse
import xlwt

def generarExcel(periodo, estudiante):
    # Se consultan los datos necesarios en la base de datos
    estudiante = Estudiantes.objects.get(pk=estudiante)
    periodo = Periodos.objects.get(pk=periodo)
    notas = Notas.objects.filter(estudiante=estudiante.id, periodos=periodo)
    justificaciones = Justificaciones.objects.filter(notas__in=notas).annotate(
            definitivaTemplate=Cast(
                Round((Coalesce(F('notas__primer_momento'), 0) + Coalesce(F('notas__segundo_momento'), 0) + Coalesce(F('notas__tercer_momento'), 0)) / 3, 2), FloatField()
                )
            )
    isCualitativa(justificaciones, 'definitivaTemplate')

    # Crea una respuesta http que correspondera a un archivo de excel y se determina el nombre
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = f'attachment; filename="{estudiante.ci}_{periodo.inicio}-{periodo.finalizacion}.xls"'

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Datos")

    # Imprime las primeras columnas
    columnas = ['Materia', 'Primer momento', 'Justificación', 'Segundo momento', 'Justificación', 'Tercer momento', 'Justificación', 'Definitiva', 'Revisión']
    for col_num, col_name in enumerate(columnas):
        ws.write(0, col_num, col_name)

    # Imprime el valor de cada fila en el archivo excel
    for fila, justificacion in enumerate(justificaciones, start=1):
            ws.write(fila, 0, justificacion.notas.materia.nombre_materia)
            if justificacion.notas.primer_momento is None:
                ws.write(fila, 1, "-")
            else:
                ws.write(fila, 1, justificacion.notas.primer_momento)
            if justificacion.primer_momento is None:
                ws.write(fila, 2, "-")
            else:
                ws.write(fila, 2, justificacion.primer_momento)
            if justificacion.notas.segundo_momento is None:
                ws.write(fila, 3, "-")
            else:
                ws.write(fila, 3, justificacion.notas.segundo_momento)                
            if justificacion.segundo_momento is None:
                ws.write(fila, 4, "-")
            else:
                ws.write(fila, 4, justificacion.segundo_momento)
            if justificacion.notas.tercer_momento is None:
                ws.write(fila, 5, "-")
            else:
                ws.write(fila, 5, justificacion.notas.tercer_momento)
            if justificacion.tercer_momento is None:
                ws.write(fila, 6, "-")
            else:
                ws.write(fila, 6, justificacion.tercer_momento)
            if justificacion.notas.definitiva is None or justificacion.notas.materia.cualitativa == 1:
                ws.write(fila, 7, justificacion.definitivaTemplate)
            else:
                ws.write(fila, 7, justificacion.notas.definitiva)
            if justificacion.notas.revision is None:
                ws.write(fila, 8, "-")
            else:
                ws.write(fila, 8, justificacion.notas.revision)
  
    #Guarda el archivo y lo retorna para enviarlo a la vista y  que el usuario lo descargue
    wb.save(response)
    return response