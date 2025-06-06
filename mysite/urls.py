"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from utils import cursosDeSeccionAjax, momentosDisponibles, periodosRevisiones, materiasReprobadasRevision

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consultar-secciones/', cursosDeSeccionAjax.consultarSecciones, name="consultarSecciones"),
    path('estudiantes/', include('estudiantes.urls'), name="estudiantes"),
    path('notas/', include('notas.urls')),
    path('', include('mainapp.urls')),
    path('consultar-momentos/', momentosDisponibles.consultarMomento, name="consultar-momento"),
    path('pensum-matricula/', include('matricula.urls'), name="pensum-matricula"),
    path('ver/',include('ver.urls'), name="ver"),
    path('periodos-revisiones/', periodosRevisiones.periodoRevisiones, name="periodosRevisiones"),
    path('materias-reprobadas-revision/', materiasReprobadasRevision.materiasReprobadasRevision, name="materiasReprobadas")
]
