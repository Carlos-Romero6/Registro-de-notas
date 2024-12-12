from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import login_excluded

# Create your views here.
@login_excluded('main')
def index(request):
    return render(request, 'index.html')

#Vista para login
@login_excluded('main')
def signin(request):
    #Renderizar el formulario al usuario
    if request.method == 'GET':
        return render(request, 'login.html')
    
    #Si no se cumplen las condiciones y el usuario envia datos al servidor, autentificar datos
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

    #Si el usuario nos se autentifica, devolverá un error
    if user is None:
        return render(request, 'login.html', {
            "error": "Nombre de usuario o contraseña incorrecta",
        })
    
    #En caso contrario, se habra logeado exitosamente
    login(request, user)
    return redirect('main')

@login_required
def main(request):
    return render(request, 'main.html')

@login_required
def signout(request):
    logout(request)
    return redirect('index')
