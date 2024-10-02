from django.shortcuts import render

from apps.home.models import MainSettings
from apps.hotel.models import Hotel


def home_view(request):
    main_settings = MainSettings.objects.first()
    # latest_hotel = Hotel.objects.order_by("-created")[:3]
    # hotel_count = Hotel.objects.all().count()
    return render(
        request,
        "home.html",
        {
            "main_settings": main_settings,
            # "latest_hotel": latest_hotel,
            # "hotel_count": hotel_count,
        },
    )
