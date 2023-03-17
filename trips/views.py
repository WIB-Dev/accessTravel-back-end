import json
from django.http import HttpResponseBadRequest
from django.shortcuts import render

from trips.models import Trips
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http.response import JsonResponse
from accesTravel.commons import getMessage
from django.core import serializers 



@csrf_exempt
def add_trip(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            departure_city = json_data['departure_city']
            destination_city = json_data['destination_city']
            departure_quater =  json_data['departure_quater']
            destination_quater = json_data['destination_quater']
            departure_date_time = json_data['departure_date_time']
            kilometer = json_data['kilometer']
            
        
            trip = Trips(departure_city=departure_city, destination_city=destination_city, departure_quater=departure_quater,
                        destination_quater=destination_quater, departure_date_time=departure_date_time, kilometer=kilometer)
            trip.save()
            msg = getMessage("Successfully add trip", 201)
            return JsonResponse(msg)
        except Exception as ex:
            msg = getMessage("Can't add trip " + str(ex), 500)
            print(ex)
            return JsonResponse(msg)
        
        
        

@csrf_exempt
def trip_detail(request, id:int):
    try:
        trip = Trips.objects.get(id=id)
                
        my_dict = {
            'id': trip.id,
            'departure_city': trip.departure_city,
            'destination_city': trip.destination_city,
            'departure_quater': trip.departure_quater,
            'destination_quater': trip.destination_quater,
            'departure_date_time': trip.departure_date_time,
            'kilometer': trip.kilometer,
        }
        data = json.dumps(my_dict)
        print(data)
        msg = getMessage(message="Successfully get trip", statut=200, data=data)
        return JsonResponse(msg)
    except Exception as ex:
        msg = getMessage("Can't add trip " + str(ex), 500)
        return JsonResponse(msg)
    
    
@csrf_exempt
def get_trips(request):
    try:
        trips = Trips.objects.all()
                
        trips_list = []
        for trip in trips:
            trip_dict = {
            'id': trip.id,
            'departure_city': trip.departure_city,
            'destination_city': trip.destination_city,
            'departure_quater': trip.departure_quater,
            'destination_quater': trip.destination_quater,
            'departure_date_time': trip.departure_date_time,
            'kilometer': trip.kilometer,
            }
            trips_list.append(trip_dict)
        data = json.dumps(trips_list)
        msg = getMessage(message="Successfully get trips", statut=200, data=data)
        return JsonResponse(msg)
    except Exception as ex:
        msg = getMessage("Can't add trips " + str(ex), 500)
        return JsonResponse(msg)



