from django.urls import path
from . import views
#Create your urls here
urlpatterns = [
    path('', views.notas, name="notas"),
    path('notas-estudiante/<int:id_estudiante>/', views.notasEstudiante, name="notas-estudiante"),
    path('cargarNota/', views.cargarNota, name="cargarNota"),
    path('modificarNota/', views.modificarNota, name="modificarNota"),
    path('cargarRevision/', views.cargarRevisiones, name="cargarRevision"),
    path('culminarPeriodo/', views.culminarPeriodo, name="culminarPeriodo")
]

