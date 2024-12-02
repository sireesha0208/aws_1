from django.db import models
from datetime import datetime

class Aircraft(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trip(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=True, blank=True)  # Make nullable temporarily
    origin = models.CharField(max_length=100,null=True, blank=True)
    destination = models.CharField(max_length=100,null=True, blank=True)
    departure_date_time = models.DateTimeField(null=True, blank=True)
    arrival_date_time = models.DateTimeField(null=True, blank=True)  # Make nullable temporarily
    flight_time = models.CharField(max_length=50, null=True, blank=True)  # Make nullable temporarily

    def __str__(self):
        return f"{self.origin} to {self.destination} on {self.departure_date_time}"


