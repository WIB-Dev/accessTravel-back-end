from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # path('', views.index),
    path('add/', views.add_trip, name='add_trip'),
    path('trip_detail/<int:id>', views.trip_detail, name='trip_detail'),
    path('get_trips/', views.get_trips, name='get_trips'),
]