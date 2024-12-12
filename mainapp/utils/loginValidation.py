from django.shortcuts import redirect, reverse, render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate

def loginProcess(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

    if user is None:
        return render(request, 'login.html', {'error': "Nombre de usuario o contraseña incorrecto"})
    login(request, user)
    return HttpResponseRedirect(reverse('main'))
