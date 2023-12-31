# Generated by Django 4.2.5 on 2023-10-09 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='POKEMON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pokemon', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='REGION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_region', models.CharField(choices=[('1', 'Kanto'), ('2', 'Johto'), ('3', 'Hoenn'), ('4', 'Sinnoh'), ('5', 'Unova'), ('6', 'Kalos'), ('7', 'Alola'), ('8', 'Galar')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TIPO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(choices=[('1', 'Agua'), ('2', 'Fuego'), ('3', 'Planta'), ('4', 'Eléctrico'), ('5', 'Hielo'), ('6', 'Lucha'), ('7', 'Normal'), ('8', 'Veneno'), ('9', 'Psíquico'), ('10', 'Roca'), ('11', 'Tierra'), ('12', 'Volador'), ('13', 'Bicho'), ('14', 'Dragón'), ('15', 'Fantasma'), ('16', 'Siniestro'), ('17', 'Acero')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TIPO_POKEMON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pokemon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_pokemon_rel', to='pokemones.pokemon')),
                ('id_tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_pokemon', to='pokemones.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='REGION_POKEMON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pokemon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_pokemon_rel', to='pokemones.pokemon')),
                ('id_region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_pokemon', to='pokemones.region')),
            ],
        ),
    ]
