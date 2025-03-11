from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReservationSerializer
from .models import Reservation
from vehicles.models import Vehicle
from datetime import datetime
from .utils import get_available_vehicle

@api_view(['GET','POST'])
def reservation_list_create(request):

    if request.method == 'GET':
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':

        try:
            start_time = datetime.fromisoformat(request.data["start_time"]).astimezone()
            end_time = datetime.fromisoformat(request.data["end_time"]).astimezone()
            v_type = request.data["v_type"].lower()

        except:
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        if start_time >= end_time:
            return Response({"error": "start_time must be before end_time"}, status=status.HTTP_400_BAD_REQUEST)

        vehicle = get_available_vehicle(v_type.lower(), start_time, end_time)

        if vehicle == None:
            return Response({"error" : f'No vehicle of type {v_type} is available during times {start_time} to {end_time}'}, status = status.HTTP_400_BAD_REQUEST)

        request.data["plate_number"] = vehicle.plate_number

        serializer = ReservationSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', 'GET', 'DELETE'])
def reservation_detail(request, pk):

    try:
        reservation = Reservation.objects.get(pk = pk)
    except Reservation.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)


    elif request.method == 'PUT':

        serializer = ReservationSerializer(reservation, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reservation.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
