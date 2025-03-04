from django.shortcuts import render
from notas.utils.definitivasCualitativas import isCualitativa
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def reincorporaciones(request)

