from rest_framework.serializers import ModelSerializer

from pokemones.models import POKEMON, TIPO, REGION, REGION_POKEMON, TIPO_POKEMON


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


class RegionPokemonSerializer(ModelSerializer):
    class Meta:
        model = REGION_POKEMON
        fields = ['id', 'id_pokemon', 'id_region']


class TipoPokemonSerializer(ModelSerializer):
    class Meta:
        model = TIPO_POKEMON
        fields = ['id', 'id_pokemon', 'id_tipo']
