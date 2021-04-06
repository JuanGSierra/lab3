from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from microservicio.models import Rutas
from microservicio.serializers import MicroservicioSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def search_route(request, route_name):
    try:
        aux = Rutas.objects.get(route_name_ruta_provisional=route_name)
        if request.method == 'GET':
            microservicio_serializer = MicroservicioSerializer(aux)
            return JsonResponse(microservicio_serializer.data)
    except Rutas.DoesNotExist:
        return JsonResponse({'message': 'The route does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def search_stop(request, stop_name):
    try:
        aux = Rutas.objects.get(route_name_ruta_provisional=stop_name)
        if request.method == 'GET':
            microservicio_serializer = MicroservicioSerializer(aux)
            return JsonResponse(microservicio_serializer.data)
    except Rutas.DoesNotExist:
        return JsonResponse({'message': 'The stop does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def search_all(request):
    aux = Rutas.objects.all()
    if request.method == 'GET':
        microservicio_serializer = MicroservicioSerializer(aux, many=True)
        return JsonResponse(microservicio_serializer.data, safe=False)
