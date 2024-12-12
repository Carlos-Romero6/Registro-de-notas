from django.urls import path
from . import views
from .utils import loginValidation

#Create your urls here
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.signin, name="login"),
    path('login-process/', loginValidation.loginProcess, name="login-process"),
    path('main/', views.main, name="main"),
    path('logout/', views.signout, name="logout"),
]
