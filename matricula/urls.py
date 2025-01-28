from django.urls import path
from . import views
from .utils import registrarPensum, registrarMateria, registrarMatricula

urlpatterns = [
    path('', views.pensum_matricula, name="pensum-matricula"),#Menú principal de pensum y matricula
    path('menu-pensum/', views.menu_pensum, name="menu-pensum"),#Menú principal de pensum
    path('menu-matricula/', views.menu_matricula, name="menu-matricula"),#Menú principal de matricula
    path('agregar/', registrarPensum.agregar, name="agregarPensum"),#Dirección url para registrar pénsum
    path('materias_pensum/<int:id_pensum>/', views.materias_pensum, name="materias_pensum"),# Menú de materias de los pénsums que recibe el id del pénsum
    path('agregar2/', registrarMateria.agregar, name="agregarMateria"),
    path('modificarMateria/', views.modificarMateria, name="modificarMateria"),#Dirección url para modificar la materia
    path('modificarPensum/', views.modificarPensum, name="modificarPensum"),#Direccón url para modificar pénsum
    path('agregarmatricula/', registrarMatricula.agregar, name="agregarMatricula"),#Dirección url para registrar matricula
    path('secciones_matricula/<int:id_matricula>/', views.secciones_matricula, name="secciones_matricula"),# Menú de secciones de las matriculas que recibe el id de la matricula
    path('modificarMatricula/', views.modificarMatricula, name="modificarMatricula"),##Direccón url para modificar la matricula
]
