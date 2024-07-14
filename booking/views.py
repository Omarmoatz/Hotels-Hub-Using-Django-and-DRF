from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Booking,Hotel,Room,RoomType


def check_avilability(request,pk,slug):
    name = request.POST.get('name','')
    email = request.POST.get('email','')
    checkin = request.POST.get('checkin','')
    checkout = request.POST.get('checkout','')
    adults = request.POST.get('adults','')
    children = request.POST.get('children','')
    hotel = get_object_or_404(Hotel,slug=slug)
    room_type = get_object_or_404(RoomType, hotel=hotel, id=pk)

    print(f'name==={name}')
    print(f'email==={email}')
    print(f'checkin==={checkin}')
    print(f'checkout==={checkout}')
    print(f'adults==={adults}')
    print(f'children==={children}')
    print(f'hotel==={hotel}')
    print(f'room_type==={room_type}')

    url = reverse('hotel:room_type_detail', args=(slug, pk))
    url_with_params = f'{url}?id={hotel.id}&name={name}&email={email}&checkin={checkin}&checkout={checkout}&adults={adults}&children={children}&room_type={room_type}'
    return HttpResponseRedirect(url_with_params)








# class CheckAvilability(generic.CreateView):
#     model = Booking
#     form_class = BokingForm
#     template_name = 'hotel/check_availability.html'
#     success_url = 'hotel/'

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context["room_type"] = models.RoomType.objects.filter(hotel =self.get_object())
#     #     return context
    

#     def form_valid(self, form):
#         slug = self.kwargs['slug']
#         room_type = self.kwargs['room_type']
#         user = self.request.user

#         hotel = get_object_or_404(Hotel, slug=slug)
#         # room_type = models.RoomType.objects.filter(hotel=hotel)
#         room = Room.objects.filter(hotel=hotel, room_type=room_type)

#         print( hotel, room, room_type,'-------------------')

#         form.instance.hotel = hotel
#         form.instance.room = room
#         form.instance.room_type = room_type


#         if user.is_authenticated:
#             form.instance.user = user

#         # self.success_url = f'/hotels/{slug}/ckeck_avilability/'
#         return super().form_valid(form) 
