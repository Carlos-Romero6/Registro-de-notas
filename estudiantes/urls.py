from django.urls import path
from utils import cursosDeSeccionAjax
from . import views

#Create your views here
urlpatterns = [
    path('consultar-secciones/', cursosDeSeccionAjax.consultarSecciones, name="consultarSecciones"),
    path('', views.menuEstudiantes, name="estudiantes"),
]
