from django.views import generic
from django.shortcuts import render, get_object_or_404

from . import models
from utils import random_numbers

class HotelList(generic.ListView):
    model = models.Hotel


class HotelDetail(generic.DetailView):
    model = models.Hotel
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel_gallery'] =  models.HotelGallery.objects.filter(hotel=self.get_object())
        context['hotel_features'] =  models.HotelFeatures.objects.filter(hotel=self.get_object())
        context['room_type'] = models.RoomType.objects.filter(hotel=self.get_object())  
        context['review'] = models.Review.objects.filter(hotel=self.get_object())  
        context['related_hotels'] = models.Hotel.objects.all()[:3]  
        # context['related_hotels'] = models.Hotel.objects.all()[:random_numbers]  
        return context
    


class RoomTypeDetail(generic.DetailView):
    model = models.RoomType
    context_object_name = 'room_type'

    def get_object(self):
        hotel_slug = self.kwargs.get('slug')
        room_type_slug = self.kwargs.get('room_type_slug')
        return get_object_or_404(models.RoomType, hotel__slug=hotel_slug, slug=room_type_slug)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = models.Room.objects.filter(room_type=self.get_object(), is_available=True)
        context["name"] = self.request.GET['name']
        context["email"] = self.request.GET['email']
        context["checkin"] = self.request.GET['checkin']
        context["checkout"] = self.request.GET['checkout']
        context["adults"] = self.request.GET['adults']
        context["children"] = self.request.GET['children']
        return context
    
    
        
