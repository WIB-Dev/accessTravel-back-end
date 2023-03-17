from django.db import models

# Create your models here.
class Trips(models.Model):
    def __str__(self) -> str:
        return super().__str__()
    # trip_id = models.CharField(max_length=255)
    departure_city = models.CharField(max_length=255)
    destination_city = models.CharField(max_length=255)
    departure_quater = models.CharField(max_length=255)
    destination_quater = models.CharField(max_length=255)
    departure_date_time = models.CharField(max_length=255)
    kilometer = models.IntegerField()