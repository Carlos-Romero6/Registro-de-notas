from django.urls import path
from . import views

#Create your urls here
urlpatterns = [
    path('', views.notas, name="notas"),
    path('notas/notas-estudiante/<int:id_estudiante>/', views.notasEstudiante, name="notas-estudiante")
]

