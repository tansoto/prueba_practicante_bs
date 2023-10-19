from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from pokemones.models import POKEMON, TIPO, REGION, REGION_POKEMON, TIPO_POKEMON
from pokemones.api.serializers import PokemonSerializer, TipoSerializer, RegionSerializer, RegionPokemonSerializer, TipoPokemonSerializer
from rest_framework import generics


class PokemonApiViewSet(ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = POKEMON.objects.all()


class TipoApiViewSet(ModelViewSet):
    serializer_class = TipoSerializer
    queryset = TIPO.objects.all()


class RegionApiViewSet(ModelViewSet):
    serializer_class = RegionSerializer
    queryset = REGION.objects.all()


class RegionPokemonApiViewSet(ModelViewSet):
    serializer_class = RegionPokemonSerializer
    queryset = REGION_POKEMON.objects.all()


class TipoPokemonApiViewSet(ModelViewSet):
    serializer_class = TipoPokemonSerializer
    queryset = TIPO_POKEMON.objects.all()
