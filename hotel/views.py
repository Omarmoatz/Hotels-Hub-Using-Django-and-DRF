from django.views import generic
from django.shortcuts import render

from . import models

class HotelList(generic.ListView):
    model = models.Hotel
