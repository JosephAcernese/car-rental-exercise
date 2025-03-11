from django.db import models

# Create your models here.
class Vehicle(models.Model):
    plate_number = models.CharField(max_length=10, primary_key=True)
    v_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.plate_number} {self.v_type}'