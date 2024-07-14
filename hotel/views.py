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
    # queryset = models.RoomType.objects.filter(slug=self.kwargs['rslug'])

    def get_queryset(self):
        queryset = super().get_queryset().filter(slug=self.kwargs['room_type_slug'])
        return queryset
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        # Return the single item from the filtered queryset
        obj = get_object_or_404(queryset)
        return obj
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = models.Room.objects.filter(room_type=self.get_object(), is_available=True)
        return context
    
    
        
