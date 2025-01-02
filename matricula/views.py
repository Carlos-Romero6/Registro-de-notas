from django.shortcuts import render, get_list_or_404, redirect 
from django.http import JsonResponse
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones, Periodos
from django.urls import reverse
from utils import pensumscursosdisponibles
# Create your views here.

def pensum_matricula(request):
    if request.method == 'GET':
        return render(request, 'menu-pensum-matricula.html')

def menu_matricula(request):
    if request.method == 'GET':
        matriculas = Matricula.objects.all()
        return render(request, 'menu-matricula.html', pensumscursosdisponibles.obtener_pensums(), {'matriculas': matriculas})
    
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

        