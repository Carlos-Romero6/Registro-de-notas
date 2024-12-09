from django.urls import path
from . import views

#Create your urls here
urlpatterns = [
    path('notas/', views.grades, name="notas"),
]
