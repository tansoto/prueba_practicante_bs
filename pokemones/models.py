# models.py

from django.db import models


class TIPO(models.Model):
    nombre_tipo = models.CharField(max_length=255, null=False)


class POKEMON(models.Model):
    nombre_pokemon = models.CharField(max_length=255, null=False)


class TIPO_POKEMON(models.Model):
    id_tipo = models.ForeignKey(
        TIPO, null=True, blank=True, on_delete=models.CASCADE, related_name='tipo_pokemon')
    id_pokemon = models.ForeignKey(
        POKEMON, null=True, blank=True, on_delete=models.CASCADE, related_name='tipo_pokemon_rel')


class REGION(models.Model):
    nombre_region = models.CharField(max_length=255, null=False)


class REGION_POKEMON(models.Model):
    id_region = models.ForeignKey(
        REGION, null=True, blank=True, on_delete=models.CASCADE, related_name='region_pokemon')
    id_pokemon = models.ForeignKey(
        POKEMON, null=True, blank=True, on_delete=models.CASCADE, related_name='region_pokemon_rel')
