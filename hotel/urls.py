from django.urls import path

from .views import HotelList, HotelDetail, RoomTypeDetail
from .api import HotelApiView

app_name = 'hotel'

  #   hotels/
urlpatterns = [
    path('', HotelList.as_view(), name='hotel_list' ),
    path('<slug:slug>', HotelDetail.as_view(), name='hotel_detail' ),
    path('<slug:slug>/<slug:room_type_slug>', RoomTypeDetail.as_view(), name='room_type_detail' ),


    #  API
    path('api/', HotelApiView.as_view(), name='hotel_list_api'),
    # path('api/<slug:slug>/', HotelDetailApi.as_view(), name='hotel_detail_api'),

]
