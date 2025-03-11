from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer
from .models import Vehicle


# Create your views here.
@api_view(['GET', 'POST'])
def vehicle_list_create(request):

    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':

        if request.data["plate_number"]:
            request.data["plate_number"] = request.data["plate_number"].lower()

        if request.data["v_type"]:
            request.data["v_type"].lower()

        serializer = VehicleSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
def vehicle_detail(request, pk):

    try:
        vehicle = Vehicle.objects.get(pk = pk)
    except Vehicle.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)


    elif request.method == 'PUT':

        serializer = VehicleSerializer(vehicle, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vehicle.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
