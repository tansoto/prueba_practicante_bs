# models.py

from django.db import models
tipos = [
    ('1', 'Agua'),
    ('2', 'Fuego'),
    ('3', 'Planta'),
    ('4', 'Eléctrico'),
    ('5', 'Hielo'),
    ('6', 'Lucha'),
    ('7', 'Normal'),
    ('8', 'Veneno'),
    ('9', 'Psíquico'),
    ('10', 'Roca'),
    ('11', 'Tierra'),
    ('12', 'Volador'),
    ('13', 'Bicho'),
    ('14', 'Dragón'),
    ('15', 'Fantasma'),
    ('16', 'Siniestro'),
    ('17', 'Acero'),
]
regiones = [('1', 'Kanto'),
            ('2', 'Johto'),
            ('3', 'Hoenn'),
            ('4', 'Sinnoh'),
            ('5', 'Unova'),
            ('6', 'Kalos'),
            ('7', 'Alola'),
            ('8', 'Galar')

            ]


class TIPO(models.Model):
    nombre_tipo = models.CharField(max_length=2, choices=tipos)


class POKEMON(models.Model):
    nombre_pokemon = models.CharField(max_length=255, null=False)


class TIPO_POKEMON(models.Model):
    id_tipo = models.ForeignKey(
        TIPO, null=True, blank=True, on_delete=models.CASCADE, related_name='tipo_pokemon')
    id_pokemon = models.ForeignKey(
        POKEMON, null=True, blank=True, on_delete=models.CASCADE, related_name='tipo_pokemon_rel')


class REGION(models.Model):
    nombre_region = models.CharField(max_length=2, choices=regiones)


class REGION_POKEMON(models.Model):
    id_region = models.ForeignKey(
        REGION, null=True, blank=True, on_delete=models.CASCADE, related_name='region_pokemon')
    id_pokemon = models.ForeignKey(
        POKEMON, null=True, blank=True, on_delete=models.CASCADE, related_name='region_pokemon_rel')
