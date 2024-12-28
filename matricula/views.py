from django.shortcuts import render
from django.http import JsonResponse
from mainapp.models import Notas, Estudiantes, Materias, Matricula, Pensum, Justificaciones, Periodos
# Create your views here.

def pensum_matricula(request):
    if request.method == 'GET':
        return render(request, 'menu-pensum-matricula.html')
    
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
        materias = Materias.objects.filter(pensum__nombre_pensum=pensum.nombre_pensum)
        return render(request, 'materias_pensum.html', {
            'materias': materias,
            'pensum': pensum
            })  

        