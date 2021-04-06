from django.db import models

class Rutas(models.Model):
    objectid = models.IntegerField(primary_key=True, null=False)
    route_id_ruta_provisional = models.IntegerField(null=False)
    route_name_ruta_provisional = models.CharField(max_length=10, null=False)
    cod_def_ruta_provisional = models.CharField(max_length=8, null=False)
    distancia_ruta_provisional = models.DecimalField(
        max_digits=11, decimal_places=8, null=False)
    denominacion_ruta_provisional = models.CharField(max_length=38, null=False)
    tipo_ruta_ruta_provisional = models.IntegerField(null=False)
    zona_origen_ruta_provisional = models.IntegerField(null=False)
    zona_destino_ruta_provisional = models.IntegerField(null=False)
    localidad_origen_ruta_provision = models.IntegerField(null=False)
    localidad_destino_ruta_provisio = models.IntegerField(null=False)
    globalid = models.CharField(max_length=38, null=False)
    st_lengthshape = models.CharField(max_length=16, null=False)
