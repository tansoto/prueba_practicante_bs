from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from pokemones.models import POKEMON, TIPO, REGION
from pokemones.api.serializers import PokemonSerializer, TipoSerializer, RegionSerializer


class PokemonApiViewSet(ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = POKEMON.objects.all()


class TipoApiViewSet(ModelViewSet):
    serializer_class = TipoSerializer
    queryset = TIPO.objects.all()


class RegionApiViewSet(ModelViewSet):
    serializer_class = RegionSerializer
    queryset = REGION.objects.all()
