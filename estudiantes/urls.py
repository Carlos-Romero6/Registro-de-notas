from django.urls import path
from .utils import formularioAjax
from . import views

#Create your views here
urlpatterns = [
    path('consultar-secciones/', formularioAjax.consultarSecciones, name="consultarSecciones"),
    path('', views.menuEstudiantes, name="estudiantes"),
]
