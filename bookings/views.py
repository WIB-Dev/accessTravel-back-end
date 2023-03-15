from django.shortcuts import render

from bookings.models import Bookings, Tickets

# Create your views here.

def add_booking(request):
    if request.method == 'POST':
        # trip_id = request.POST.get('name')
        booking_id = request.POST.get('booking_id')
        booking_date_time = request.POST.get('booking_date_time')
        trip_id =  request.POST.get('trip_id')
        tickets_list = request.POST.get('tickets_list')
        # kilometer = request.POST.get('kilometer')
        booking = Bookings(booking_id=booking_id, booking_date_time=booking_date_time, trip_id=trip_id)
        # trip = Trips(departure_city=departure_city, destination_city=destination_city, departure_quater=departure_quater,
        #              destination_quater=destination_quater, departure_date_time=departure_date_time, kilometer=kilometer)
        booking.save()
        tickets_list = list(tickets_list)
        for ticket in tickets_list:
            add_ticket(booking_id=ticket.bbooking_id)
    # return render(request)
    
    
def add_ticket(request, booking_id:str, passenger_name = None):
    ticket = Tickets(booking_id=booking_id, passenger_name=passenger_name)
    ticket.save()