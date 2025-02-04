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

    # Crea el objeto de la clase que corresponde a la hoja de excel
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("Datos")

    # Creación de un estilo para los campos de la hoja de cálculo
    estiloCampo = xlwt.XFStyle()
    # Creación de una fuente para el estilo
    fuente = xlwt.Font()
    fuente.bold = True
    estiloCampo.font = fuente
    # Creación de un patron para el estilo
    patronCampo = xlwt.Pattern()
    patronCampo.pattern = xlwt.Pattern.SOLID_PATTERN
    patronCampo.pattern_fore_colour = 7
    estiloCampo.pattern = patronCampo

    # Creación de un estilo para los nombres de las materias en la hoja de cálculo
    estiloMateria = xlwt.XFStyle()
    # Creación de un patrón para el estilo
    patronMateria = xlwt.Pattern()
    patronMateria.pattern = xlwt.Pattern.SOLID_PATTERN
    patronMateria.pattern_fore_colour = 22
    estiloMateria.pattern = patronMateria

    # Creación de un estilo para los valores de la hoja de cálculo
    estiloValor = xlwt.XFStyle()
    # Creación de un patrón para el estilo
    patronValor = xlwt.Pattern()
    patronValor.pattern = xlwt.Pattern.SOLID_PATTERN
    patronValor.pattern_fore_colour = 5
    estiloValor.pattern = patronValor

    # Imprime las primeras columnas
    columnas = ['Materia', 'Primer momento', 'Justificación', 'Segundo momento', 'Justificación', 'Tercer momento', 'Justificación', 'Definitiva', 'Revisión']
    for columna, campo in enumerate(columnas):
        worksheet.write(0, columna, campo, estiloCampo)

    # Imprime el valor de cada fila en el archivo excel
    for fila, justificacion in enumerate(justificaciones, start=1):
            worksheet.write(fila, 0, justificacion.notas.materia.nombre_materia, estiloMateria)
            if justificacion.notas.primer_momento is None:
                worksheet.write(fila, 1, "-", estiloValor)
            else:
                worksheet.write(fila, 1, justificacion.notas.primer_momento, estiloValor)
            if justificacion.primer_momento is None:
                worksheet.write(fila, 2, "-", estiloValor)
            else:
                worksheet.write(fila, 2, justificacion.primer_momento, estiloValor)
            if justificacion.notas.segundo_momento is None:
                worksheet.write(fila, 3, "-", estiloValor)
            else:
                worksheet.write(fila, 3, justificacion.notas.segundo_momento, estiloValor)                
            if justificacion.segundo_momento is None:
                worksheet.write(fila, 4, "-", estiloValor)
            else:
                worksheet.write(fila, 4, justificacion.segundo_momento, estiloValor)
            if justificacion.notas.tercer_momento is None:
                worksheet.write(fila, 5, "-", estiloValor)
            else:
                worksheet.write(fila, 5, justificacion.notas.tercer_momento, estiloValor)
            if justificacion.tercer_momento is None:
                worksheet.write(fila, 6, "-", estiloValor)
            else:
                worksheet.write(fila, 6, justificacion.tercer_momento, estiloValor)
            if justificacion.notas.definitiva is None or justificacion.notas.materia.cualitativa == 1:
                worksheet.write(fila, 7, justificacion.definitivaTemplate)
            else:
                worksheet.write(fila, 7, justificacion.notas.definitiva)
            if justificacion.notas.revision is None:
                worksheet.write(fila, 8, "-")
            else:
                worksheet.write(fila, 8, justificacion.notas.revision)
  
    #Guarda el archivo y lo retorna para enviarlo a la vista y  que el usuario lo descargue
    workbook.save(response)
    return response