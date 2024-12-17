from django.urls import path
from . import views

#Create your views here
urlpatterns = [
    path('', views.menuEstudiantes, name="estudiantes"),
    path('buscar/', views.busquedaEstudiantes, name="me-buscar-estudiantes")
]
