import json
from django.shortcuts import render
from accesTravel.commons import getMessage

from bookings.models import Bookings, Tickets
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def add_booking(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            # trip_id = request.POST.get('name')
            booking_id = json_data['booking_id']
            booking_date_time = json_data['booking_date_time']
            trip_id =  json_data['trip_id']
            tickets_number = json_data['tickets_number']
            
            booking = Bookings(booking_id=booking_id, booking_date_time=booking_date_time, trip_id=trip_id, tickets_number=tickets_number)
            booking.save()
            # tickets_list = list(tickets_list)
            for ticket in range(tickets_number):
                add_ticket(booking_id=booking_id)
            msg = getMessage("Seccessful add bookings", 200)
            return JsonResponse(msg)
        except Exception as ex:
            msg = getMessage("Can't add bookings " + str(ex), 500)
            return JsonResponse(msg)
    
    
def add_ticket(booking_id:str, passenger_name = None):
    try:
        ticket = Tickets(booking_id=booking_id)
        ticket.save()
    except Exception as ex:
        print("Error: " + str(ex))
        
        
        

@csrf_exempt
def booking_detail(request, id:int):
    try:
        booking = Bookings.objects.get(id=id)
                
        my_dict = {
            'id': booking.id,
            'booking_id': booking.booking_id,
            'booking_date_time': booking.booking_date_time,
            'trip_id': booking.trip_id,
            'tickets_number': booking.tickets_number,
        }
        data = json.dumps(my_dict)
        print(data)
        msg = getMessage(message="Successfully get trip", statut=200, data=data)
        return JsonResponse(msg)
    except Exception as ex:
        msg = getMessage("Can't add trip " + str(ex), 500)
        return JsonResponse(msg)
    
    
@csrf_exempt
def get_bookings(request):
    try:
        trips = Bookings.objects.all()
                
        bookings_list = []
        for booking in trips:
            booking_dict = {
            'id': booking.id,
            'booking_id': booking.booking_id,
            'booking_date_time': booking.booking_date_time,
            'trip_id': booking.trip_id,
            'tickets_number': booking.tickets_number,
            }
            bookings_list.append(booking_dict)
        data = json.dumps(bookings_list)
        msg = getMessage(message="Successfully get trips", statut=200, data=data)
        return JsonResponse(msg)
    except Exception as ex:
        msg = getMessage("Can't add trips " + str(ex), 500)
        return JsonResponse(msg)