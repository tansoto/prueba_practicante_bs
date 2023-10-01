from django.shortcuts import render, redirect
from pokemones.formspokemon import PokemonForm
from .models import TIPO, POKEMON, TIPO_POKEMON, REGION, REGION_POKEMON


def Menu(request):
    return render(request, 'Menu.html')


def CRUD(request):
    # Obtén la cadena de búsqueda del parámetro GET
    query = request.GET.get('q', '')

    # Filtra los Pokémon que coinciden con la búsqueda
    pokemon = POKEMON.objects.filter(nombre_pokemon__icontains=query)
    tipo_pokemon = TIPO_POKEMON.objects.all()
    region_pokemon = REGION_POKEMON.objects.all()
    tipo = TIPO.objects.all()
    region = REGION.objects.all()

    formulario = PokemonForm(request.POST or None, request.FILES or None)
    print(formulario)

    data = {
        'pokemones': pokemon,
        'tipos': tipo,
        'regiones': region,
        'formulario': formulario,
        'tipos_pokemones': tipo_pokemon,
        'regiones_pokemones': region_pokemon,
    }
    return render(request, 'CRUD.html', data)


def agregarpokemon(request):
    nombre = request.POST['nombre_pokemon']
    region = request.POST['region']
    tipo = request.POST['tipo']

    nuevo_pokemon = POKEMON.objects.create(nombre_pokemon=nombre)
    region_pokemon = REGION.objects.create(nombre_region=region)
    tipo_pokemon = TIPO.objects.create(nombre_tipo=tipo)

    id_pokemon_tipo = TIPO_POKEMON.objects.create(
        id_pokemon_id=nuevo_pokemon.id, id_tipo_id=tipo_pokemon.id)
    id_pokemon_region = REGION_POKEMON.objects.create(
        id_pokemon_id=nuevo_pokemon.id, id_region_id=region_pokemon.id)

    print(f"Nombre: {nombre}")
    print(f"Región : {region}")
    print(f"Tipo: {tipo}")

    # Agregar mensajes de depuración
    print(f"Nuevo Pokémon ID: {nuevo_pokemon.id}")
    print(f"Nuevo Pokémon region ID: {region_pokemon.id}")
    print(f"Nuevo Pokémon tipo ID: {tipo_pokemon.id}")

    print(f"Nuevo Pokémon region: {region_pokemon.nombre_region}")
    print(f"nuevo pokemon nombre: {nuevo_pokemon.nombre_pokemon}")
    return redirect('../CRUD/')


def eliminarPokemon(request, id_pokemon):
    pokemon = POKEMON.objects.get(id=id_pokemon)
    tipo_pokemon = TIPO_POKEMON.objects.get(id_pokemon=id_pokemon)
    region_pokemon = REGION_POKEMON.objects.get(id_pokemon=id_pokemon)

    region = REGION.objects.get(id=region_pokemon.id_region_id)
    tipo = TIPO.objects.get(id=tipo_pokemon.id_tipo_id)

    pokemon.delete()
    region.delete()
    tipo.delete()

    return redirect('../../CRUD/')


def editarPokemon(request, id_pokemon):
    pokemon = POKEMON.objects.get(id=id_pokemon)
    tipo_pokemon = TIPO_POKEMON.objects.get(id_pokemon=id_pokemon)
    region_pokemon = REGION_POKEMON.objects.get(id_pokemon=id_pokemon)

    region = REGION.objects.get(id=region_pokemon.id_region_id)
    tipo = TIPO.objects.get(id=tipo_pokemon.id_tipo_id)

    data = {'pokemones': pokemon, 'tipos': tipo, 'regiones': region,
            'tipos_pokemones': tipo_pokemon, 'regiones_pokemones': region_pokemon}
    return render(request, 'Editar_pokemon.html', data)


def editarPokemon2(request):
    # nombre de la variable en el modelo = variable obtenida de html
    id_pokemon = request.POST['pokemon_id']
    id_region = request.POST['region_id']
    id_tipo = request.POST['tipo_id']
    nombre = request.POST['nombre_pokemon']
    region = request.POST['region']
    tipo = request.POST['tipo']

    print(f" Pokémon ID en editar: {id_pokemon}")
    print(f" Región ID en editar: {id_region}")
    print(f" Tipo ID en editar: {id_tipo}")

    # actualizamos cada atributo

    pokemon_actualizado = POKEMON.objects.get(id=id_pokemon)
    region_actualizada = REGION.objects.get(id=id_region)
    tipo_actualizado = TIPO.objects.get(id=id_tipo)

    pokemon_actualizado.nombre_pokemon = nombre
    region_actualizada.nombre_region = region
    tipo_actualizado.nombre_tipo = tipo

    pokemon_actualizado.save()
    region_actualizada.save()
    tipo_actualizado.save()

    return redirect('../../CRUD/')
