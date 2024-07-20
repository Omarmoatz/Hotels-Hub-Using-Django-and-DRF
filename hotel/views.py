from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime

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
    
    
def selected_rooms(request):
    rooms_price = 0
    rooms_list = []
    if 'room_selection_obj' in request.session:
        for id, item in request.session['room_selection_obj'].items():
            hotel_id = int(item['hotel_id'])
            room_id = int(item['room_id'])
            checkin = item['checkin']
            checkout = item['checkout']
            adults = int(item['adults'])
            children = int(item['children'])

            room = models.Room.objects.get(id=room_id)
            rooms_list.append({
                'room_price': room.price, 
                'room_view': room.view, 
                'room_beds_num': room.beds_num, 
                'room_room_type': room.room_type
            })
            rooms_price += float(room.price ) 
            
        print(rooms_list)
        hotel = models.Hotel.objects.get(id=hotel_id)

        date_format = '%Y-%m-%d'
        chickin_date = datetime.strptime( checkin, date_format)
        chickout_date = datetime.strptime( checkout, date_format)
        total_days = (chickout_date - chickin_date).days 


        total_cost = float(rooms_price * total_days) 

        context = {
            'selected_rooms': request.session['room_selection_obj'],
            'hotel': hotel,
            'rooms_list': rooms_list,
            'checkin': checkin ,
            'checkout': checkout ,
            'total_days': total_days,
            'adults' : adults,
            'children': children,
            'total_cost': round(total_cost,2) 
        }

        return render(request, 'hotel/rooms_selected.html', context)
    
    else:
        messages.warning(request, 'You dont have any Rooms Booked Yet!')
        return redirect('/')


