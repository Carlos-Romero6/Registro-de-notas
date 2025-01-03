from django.urls import path
from . import views
from .utils import registrarPensum, registrarMateria, registrarMatricula

urlpatterns = [
    path('', views.pensum_matricula, name="pensum-matricula"),
    path('menu-pensum/', views.menu_pensum, name="menu-pensum"),
    path('menu-matricula/', views.menu_matricula, name="menu-matricula"),
    path('agregar/', registrarPensum.agregar, name="agregarPensum"),
    path('materias_pensum/<int:id_pensum>/', views.materias_pensum, name="materias_pensum"),
    path('agregar2/', registrarMateria.agregar, name="agregarMateria"),
    path('modificarMateria/', views.modificarMateria, name="modificarMateria"),
    path('modificarPensum/', views.modificarPensum, name="modificarPensum"),
    path('agregarmatricula/', registrarMatricula.agregar, name="agregarMatricula"),
]
