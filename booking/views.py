from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Booking,Hotel,Room,RoomType
from .forms import BokingForm


class CheckAvilability(generic.CreateView):
    model = Booking
    form_class = BokingForm
    template_name = 'hotel/check_availability.html'
    success_url = 'hotel/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["room_type"] = models.RoomType.objects.filter(hotel =self.get_object())
    #     return context
    

    def form_valid(self, form):
        slug = self.kwargs['slug']
        room_type = self.kwargs['room_type']
        user = self.request.user

        hotel = get_object_or_404(Hotel, slug=slug)
        # room_type = models.RoomType.objects.filter(hotel=hotel)
        room = Room.objects.filter(hotel=hotel, room_type=room_type)

        print( hotel, room, room_type,'-------------------')

        form.instance.hotel = hotel
        form.instance.room = room
        form.instance.room_type = room_type


        if user.is_authenticated:
            form.instance.user = user

        # self.success_url = f'/hotels/{slug}/ckeck_avilability/'
        return super().form_valid(form) 
