from rest_framework.routers import DefaultRouter
from pokemones.api.views import PokemonApiViewSet, TipoApiViewSet, RegionApiViewSet, RegionPokemonApiViewSet, TipoPokemonApiViewSet, TipoPokemonApiViewSet

router_pokemones = DefaultRouter()
router_tipo = DefaultRouter()
router_region = DefaultRouter()
router_region_pokemon = DefaultRouter()
router_tipo_pokemon = DefaultRouter()

router_pokemones.register(
    prefix='pokemones', viewset=PokemonApiViewSet, basename='pokemones')

router_tipo.register(prefix='tipo', viewset=TipoApiViewSet, basename='tipo')

router_region.register(
    prefix='region', viewset=RegionApiViewSet, basename='region')

router_region_pokemon.register(
    prefix='region_pokemon', viewset=RegionPokemonApiViewSet, basename='region_pokemon')

router_tipo_pokemon.register(
    prefix='tipo_pokemon', viewset=TipoPokemonApiViewSet, basename='tipo_pokemon')
