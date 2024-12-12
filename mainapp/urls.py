from django.urls import path
from . import views

#Create your urls here
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.signin, name="login"),
    path('main/', views.main, name="main"),
    path('logout/', views.signout, name="logout"),
]
