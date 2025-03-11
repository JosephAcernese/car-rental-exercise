from django.db import models
from vehicles.models import Vehicle

class Reservation(models.Model):
    plate_number = models.ForeignKey(Vehicle, to_field = "plate_number", on_delete=models.CASCADE)
    v_type = models.CharField(max_length=10)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.plate_number} {self.v_type} {self.start_time} {self.end_time}'