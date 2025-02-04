from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .decorators import login_excluded
from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
@login_excluded('main')
def index(request):
    return render(request, 'index.html')

#Vista para login
@login_excluded('main')
def signin(request):
    return render(request, 'login.html')

@login_required
def main(request):
    user = request.user
    return render(request, 'main.html',{
        'user': user
    })

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
