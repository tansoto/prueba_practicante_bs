from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    desciption = models.CharField(max_length=50)


class TIPO(models.Model):
    tipo = models.CharField(max_length=50)


class POKEMON(models.Model):
    nombre_pokemon = models.CharField(max_length=50, verbose_name='Nombre')


class TIPO_POKEMON(models.Model):
    id_tipo = models.ForeignKey(
        TIPO, null=True, blank=True, on_delete=models.CASCADE)
    id_pokemon = models.ForeignKey(
        POKEMON, null=True, blank=True, on_delete=models.CASCADE)


class REGION(models.Model):
    region = models.CharField(max_length=50)


class REGION_POKEMON(models.Model):
    id_region = models.ForeignKey(
        TIPO, null=True, blank=True, on_delete=models.CASCADE)
    id_pokemon = models.ForeignKey(
        POKEMON, null=True, blank=True, on_delete=models.CASCADE)
