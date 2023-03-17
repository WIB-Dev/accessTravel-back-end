from django.db import models

# Create your models here.
class Bookings(models.Model):
    def __str__(self) -> str:
        return super().__str__()
    booking_id = models.CharField(max_length=255)
    booking_date_time = models.CharField(max_length=255, default="0000000000")
    trip_id = models.IntegerField()
    tickets_number = models.IntegerField(default=1)
    
    
    

class Tickets(models.Model):
    def __str__(self) -> str:
        return super().__str__()
    passenger_name = models.CharField(max_length=255, default='None')
    booking_id = models.CharField(max_length=255, default=0)