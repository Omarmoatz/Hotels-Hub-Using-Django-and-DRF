from django.shortcuts import render

from .models import MainSettings

def home_view(request):
    main_settings = MainSettings.objects.first()
    return render(request, 'home.html', {'main_settings': main_settings})
