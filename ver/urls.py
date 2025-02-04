from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ver, name="ver"),
    path('secciones/<int:id_matricula>', views.secciones, name="secciones"),
    path('estudiantes/', views.estudiantes, name="estudiantesVer"),
    path('verNotas/<int:curso>/', views.notasVer, name="verNotas"),
    path('descargar-notas/', views.descargarExcel, name="descargarExcel"),
]