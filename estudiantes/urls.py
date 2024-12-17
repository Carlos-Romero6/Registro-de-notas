from django.urls import path
from utils import cursosDeSeccionAjax
from . import views

#Create your views here
urlpatterns = [
    path('', views.menuEstudiantes, name="estudiantes"),
]
