from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # path('', views.index),
    path('bookings/add/', views.add_booking, name='add_booking'),
]