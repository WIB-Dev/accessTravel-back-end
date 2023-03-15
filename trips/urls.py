from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # path('', views.index),
    path('trips/add/', views.add_trip, name='add_trip'),
]