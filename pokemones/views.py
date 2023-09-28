from django.shortcuts import render
from .models import POKEMON, REGION_POKEMON, TIPO, TIPO_POKEMON, Task
# Create your views here.


def list_tasks(request):
    return render(request, 'list_tasks.html')


def CRUD(request):
    pokemon = POKEMON.objects.all()
    tipo = TIPO_POKEMON.objects.all()
    data = {'productos': pokemon, 'tipo': tipo, }
    return render(request, 'CRUD.html', data)
