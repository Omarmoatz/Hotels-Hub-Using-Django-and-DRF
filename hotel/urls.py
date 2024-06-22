from django.urls import path

from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.HotelList.as_view(), name='hotel_list' )
]
