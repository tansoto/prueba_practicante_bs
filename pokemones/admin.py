from django.contrib import admin
from pokemones.models import POKEMON, REGION, TIPO, REGION_POKEMON, TIPO_POKEMON

# Register your models here.


@admin.register(POKEMON)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_pokemon']


@admin.register(REGION)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_region']


@admin.register(TIPO)
class TipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_tipo']


@admin.register(REGION_POKEMON)
class RegionPokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_pokemon', 'id_region']


@admin.register(TIPO_POKEMON)
class TipoPokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_pokemon', 'id_tipo']


0
