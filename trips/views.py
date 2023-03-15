from django.shortcuts import render

from trips.models import Trips


# Create your views here.


def add_trip(request):
    if request.method == 'POST':
        # trip_id = request.POST.get('name')
        departure_city = request.POST.get('departure_city')
        destination_city = request.POST.get('destination_city')
        departure_quater =  request.POST.get('departure_quater')
        destination_quater = request.POST.get('destination_quater')
        departure_date_time = request.POST.get('departure_date_time')
        kilometer = request.POST.get('kilometer')
        trip = Trips(departure_city=departure_city, destination_city=destination_city, departure_quater=departure_quater,
                     destination_quater=destination_quater, departure_date_time=departure_date_time, kilometer=kilometer)
        trip.save()
    # return render(request)
