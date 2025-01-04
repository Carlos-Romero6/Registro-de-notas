from .utils import eliminarEstudiante, registrarEstudiante, editarEstudiante
from django.urls import path
from . import views

#Create your views here
urlpatterns = [
    path('', views.menuEstudiantes, name="estudiantes"),
    path('buscar/', views.busquedaEstudiantes, name="me-buscar-estudiantes"),
    path('buscar/eliminar/<int:estudiante_id>/', eliminarEstudiante.porID, name="eliminar-estudiante"),
    path('agregar/', registrarEstudiante.agregar, name="agregarEstudiante"),
    path('obtener-datos/', editarEstudiante.obtenerDatos, name="obtenerDatosEstudiante"),
    path('actualizar/<int:estudiante_id>/', editarEstudiante.actualizar, name="actualizarEstudiante"),
]
