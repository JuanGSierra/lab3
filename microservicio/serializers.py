from rest_framework import serializers
from microservicio.models import Rutas


class MicroservicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rutas
        fields = ('objectid',
                  'route_id_ruta_provisional',
                  'route_name_ruta_provisional',
                  'cod_def_ruta_provisional',
                  "distancia_ruta_provisional",
                  "denominacion_ruta_provisional",
                  "tipo_ruta_ruta_provisional",
                  "zona_origen_ruta_provisional",
                  "zona_destino_ruta_provisional",
                  "localidad_origen_ruta_provision",
                  "localidad_destino_ruta_provisio",
                  "globalid",
                  "st_lengthshape"
                  )
