from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.shortcuts import render, get_object_or_404

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
    
class CheckAvilability(generic.CreateView):
    model = models.Booking
    fields = '__all__'
    template_name = 'hotel/check_availability.html'
    success_url = 'hotel/'

    def form_valid(self, form):
        slug = self.kwargs['slug']
        hotel = get_object_or_404(models.hotel, slug=slug)
        form.instance.hotel = hotel
        # self.success_url = f'/hotels/{slug}/ckeck_avilability/'
        return super().form_valid(form)  
    
        
