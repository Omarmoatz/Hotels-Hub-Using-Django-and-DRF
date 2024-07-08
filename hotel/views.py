from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.shortcuts import render, get_object_or_404

from . import models
from .forms import BokingForm
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
    
class CheckAvilability(generic.CreateView):
    model = models.Booking
    form_class = BokingForm
    template_name = 'hotel/check_availability.html'
    success_url = 'hotel/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["room_type"] = models.RoomType.objects.filter(hotel =self.get_object().hotel)
    #     return context
    

    def form_valid(self, form):
        slug = self.kwargs['slug']
        user = self.request.user

        hotel = get_object_or_404(models.Hotel, slug=slug)
        room = models.Room.objects.filter(hotel=hotel)
        room_type = models.RoomType.objects.filter(hotel=hotel)

        form.instance.hotel = hotel
        form.instance.room = room
        form.instance.room_type = room_type

        if user.is_authenticated:
            form.instance.user = user

        # self.success_url = f'/hotels/{slug}/ckeck_avilability/'
        return super().form_valid(form)  
    
        
