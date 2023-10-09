from rest_framework.serializers import ModelSerializer

from pokemones.models import POKEMON, TIPO, REGION


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = POKEMON
        fields = ['id', 'nombre_pokemon']


class TipoSerializer(ModelSerializer):
    class Meta:
        model = TIPO
        fields = ['id', 'nombre_tipo']


class RegionSerializer(ModelSerializer):
    class Meta:
        model = REGION
        fields = ['id', 'nombre_region']
