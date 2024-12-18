from django.urls import path
from . import views
from utils import eliminarEstudiante

#Create your views here
urlpatterns = [
    path('', views.menuEstudiantes, name="estudiantes"),
    path('buscar/', views.busquedaEstudiantes, name="me-buscar-estudiantes"),
    path('buscar/eliminar/<int:estudiante_id>/', eliminarEstudiante.porID, name="eliminar-estudiante"),
]
