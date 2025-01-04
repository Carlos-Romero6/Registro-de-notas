from django.shortcuts import render, get_list_or_404, redirect 
from django.http import JsonResponse
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones, Periodos
from django.urls import reverse
from django.db.models import Count
# Create your views here.

def pensum_matricula(request):
    if request.method == 'GET':
        return render(request, 'menu-pensum-matricula.html')

def menu_matricula(request):
    if request.method == 'GET':
        matriculas = Matricula.objects.filter(curso__range=(1, 5))
        pensums = Pensum.objects.all()
        num_matriculas_curso_1 = Matricula.objects.filter(curso=1).count()
        return render(request, 'menu-matricula.html', {
            'matriculas': matriculas,
            'pensums': pensums,
            'matriculas_curso_1': num_matriculas_curso_1
            })
    
def menu_pensum(request):
    if request.method == 'GET':
        pensums = Pensum.objects.all()
        return render(request, 'menu-pensum.html', {'pensums': pensums})
    #elif request.method == 'POST':
                
            #MATERIAS = Materias.objects.filter(pensum__nombre_pensum = request.POST['pensum1'])
            #return render(request, 'materias-pensum.html',{
            #'materias': MATERIAS,
            #'pensum': request.POST['pensum1'],
            #})

def materias_pensum(request, id_pensum):
    if request.method == 'GET':
        pensum = Pensum.objects.get(pk=id_pensum)
        matriculas = Matricula.objects.filter(pensum=pensum.id)
        materias = Materias.objects.filter(pensum=pensum.id)
        return render(request, 'materias_pensum.html', {
            'materias': materias,
            'pensum': pensum,
            "matriculas": matriculas
            })  

def modificarMateria(request):
    try:
        if request.method == 'POST':
            print(request.POST)
            pensum_id = request.POST.get('pensummateria_modificar')
            print(pensum_id)
            materia_id = request.POST.get('materiaid_modificar')
            print(materia_id)
            curso = request.POST.get('cursomateria_modificar')
            cualitativa = request.POST.get('cualitativomateria_modificar')
            nombre_materia = request.POST.get('nombremateria_modificar')
            pensum = Pensum.objects.get(pk=pensum_id)
            materia = Materias.objects.get(pk=materia_id, pensum=pensum)
            materia.nombre_materia = nombre_materia
            materia.curso = curso
            materia.cualitativa = cualitativa
            materia.save()
        
        return JsonResponse({'success': True, 'message': "La materia ha sido modificada exitosamente."})
    
    except:
        return JsonResponse({'success': False, 'message': 'Ha ocurrido un fallo inesperado'})
    
def modificarPensum(request):
    try:
        if request.method == 'POST':
            print(request.POST)
            pensum_id = request.POST.get('pensumid_modificar')
            print(pensum_id)
            nombre_pensum = request.POST.get('nombre_pensum_modificar')
            pensum = Pensum.objects.get(pk=pensum_id)
            pensum.nombre_pensum = nombre_pensum
            pensum.save()
        
        return JsonResponse({'success': True, 'message': "El Pensum ha sido modificado exitosamente."})
    
    except:
        return JsonResponse({'success': False, 'message': 'Ha ocurrido un fallo inesperado'})

def secciones_matricula(request, id_matricula):
    if request.method == 'GET':
        matricula = Matricula.objects.get(pk=id_matricula)
        pensums = Pensum.objects.all()
        secciones = ['A', 'B', 'C', 'D', 'E', 'F'][:matricula.n_secciones]

        pensum = Pensum.objects.get(pk=matricula.pensum.id)
        return render(request, 'secciones_matricula.html', {
            'pensum': pensum,
            'matricula': matricula,
            'secciones': secciones,
            'pensums': pensums
            })

def modificarMatricula(request):
    try:
        if request.method == 'POST':
            print(request.POST)
            pensum_id_nuevo = request.POST.get('pensumnuevo_modificar')
            print(pensum_id_nuevo)
            pensum_id = request.POST.get('pensum_modificar')
            print(pensum_id)
            matricula_id = request.POST.get('matriculaid_modificar')
            print(matricula_id)
            curso = request.POST.get('curso_modificar')
            promocion = request.POST.get('promocion_modificar')
            n_secciones = request.POST.get('secciones_modificar')
            pensum = Pensum.objects.get(pk=pensum_id)
            pensum_nuevo = Pensum.objects.get(pk=pensum_id_nuevo)
            matricula = Matricula.objects.get(pk=matricula_id, pensum=pensum)
            matricula.promocion = promocion
            matricula.curso = curso
            matricula.n_secciones = n_secciones
            matricula.pensum = pensum_nuevo
            matricula.save()
        
        return JsonResponse({'success': True, 'message': "La matricula ha sido modificada exitosamente."})
    
    except:
        return JsonResponse({'success': False, 'message': 'Ha ocurrido un fallo inesperado'})