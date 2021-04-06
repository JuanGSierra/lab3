# Generated by Django 3.1.7 on 2021-04-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('objectid', models.IntegerField(primary_key=True, serialize=False)),
                ('route_id_ruta_provisional', models.IntegerField()),
                ('route_name_ruta_provisional', models.CharField(max_length=10)),
                ('cod_def_ruta_provisional', models.CharField(max_length=8)),
                ('distancia_ruta_provisional', models.DecimalField(decimal_places=8, max_digits=11)),
                ('denominacion_ruta_provisional', models.CharField(max_length=38)),
                ('tipo_ruta_ruta_provisional', models.IntegerField()),
                ('zona_origen_ruta_provisional', models.IntegerField()),
                ('zona_destino_ruta_provisional', models.IntegerField()),
                ('localidad_origen_ruta_provision', models.IntegerField()),
                ('localidad_destino_ruta_provisio', models.IntegerField()),
                ('globalid', models.CharField(max_length=38)),
                ('st_lengthshape', models.CharField(max_length=16)),
            ],
        ),
    ]
