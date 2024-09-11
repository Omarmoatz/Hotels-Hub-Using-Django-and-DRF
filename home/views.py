from django.shortcuts import render

from .models import MainSettings
from hotel.models import Hotel

def home_view(request):
    main_settings = MainSettings.objects.first()
    latest_hotel = Hotel.objects.order_by('-created')[:3]
    hotel = Hotel.objects.all()
    return render(request, 'home.html', {'main_settings': main_settings,
                                         'hotel':hotel,
                                         'latest_hotel':latest_hotel})
