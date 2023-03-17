from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    # path('', views.index),
    path('add/', views.add_booking, name='add_booking'),
    path('booking_detail/<int:id>', views.booking_detail, name='booking_detail'),
    path('get_bookings/', views.get_bookings, name='get_bookings'),
]