from rest_framework.routers import DefaultRouter
from pokemones.api.views import PokemonApiViewSet, TipoApiViewSet, RegionApiViewSet

router_pokemones = DefaultRouter()
router_tipo = DefaultRouter()
router_region = DefaultRouter()

router_pokemones.register(
    prefix='pokemones', viewset=PokemonApiViewSet, basename='pokemones')

router_tipo.register(prefix='tipo', viewset=TipoApiViewSet, basename='tipo')

router_region.register(
    prefix='region', viewset=RegionApiViewSet, basename='region')
