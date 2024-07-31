from django.urls import path

from . import views
from . import api

app_name = 'hotel'

  #   hotels/
urlpatterns = [
    path('', views.HotelList.as_view(), name='hotel_list' ),
    path('<slug:slug>/', views.HotelDetail.as_view(), name='hotel_detail' ),
    path('<slug:slug>/<slug:room_type_slug>/', views.RoomTypeDetail.as_view(), name='room_type_detail' ),


    #  API
    path('api', api.hotel_list, name='hotel_list_api')
]
