from django.db import models

# Create your models here.
class Bookings(models.Model):
    def __str__(self) -> str:
        return super().__str__()
    booking_id = models.CharField(max_length=255)
    booking_date_time = models.CharField(max_length=255)
    trip_id = models.IntegerField()
    tickets_list = models.CharField(max_length=255)
    
    
    

class Tickets(models.Model):
    def __str__(self) -> str:
        return super().__str__()
    passenger_name = models.CharField(max_length=255)
    booking_id = Bookings.booking_id