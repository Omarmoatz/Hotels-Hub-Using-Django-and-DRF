from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.shortcuts import render

from . import models
from utils import random_numbers

class HotelList(generic.ListView):
    model = models.Hotel

class HotelDetail(generic.DetailView):
    model = models.Hotel
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['hotel_gallery'] =  models.HotelGallery.objects.filter(hotel=self.get_object())
        context['hotel_features'] =  models.HotelFeatures.objects.filter(hotel=self.get_object())
        context['room_type'] = models.RoomType.objects.filter(hotel=self.get_object())  
        context['review'] = models.Review.objects.filter(hotel=self.get_object())  
        context['related_hotels'] = models.Hotel.objects.all()[:3]  
        # context['related_hotels'] = models.Hotel.objects.all()[:random_numbers]  
        return context
    
class BookingHotel(generic.CreateView):
    model = models.Booking
    fields = ['full_name', 'email', 'room_type']
    success_url = ''
    
        
