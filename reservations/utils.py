from rest_framework import status
from .serializers import ReservationSerializer
from .models import Reservation
from vehicles.models import Vehicle
from datetime import datetime


def get_available_vehicle(v_type, start_time, end_time):
    '''
    Returns a vehicle with a matching type and open availability, none otherwise
    '''

    vehicles = Vehicle.objects.filter(v_type = v_type)
    for vehicle in vehicles:

        reservations = Reservation.objects.filter(plate_number = vehicle.plate_number)
        is_valid = True

        for reservation in reservations:

            # Check for overlap with time intervals
            if max(reservation.start_time, start_time) <= min(reservation.end_time, end_time):
                is_valid = False
                break

        if is_valid:
            return vehicle

    return None