from django.shortcuts import render

from .models import MainSettings
from hotel.models import Hotel

def home_view(request):
    main_settings = MainSettings.objects.first()
    hotel = Hotel.objects.all()[:3]
    return render(request, 'home.html', {'main_settings': main_settings,
                                         'hotel':hotel})
