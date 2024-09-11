from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HotelList, HotelDetail, RoomTypeDetail
from hotel.api.views import HotelApiView, RoomTypeApiView

app_name = 'hotel'

router = DefaultRouter()
router.register('api', HotelApiView, basename='hotel')
router.register(r'api/(?P<hotel_pk>\d+)/room-type', RoomTypeApiView, basename='roomtype') 
 
#   hotels/
urlpatterns = [
    path('', HotelList.as_view(), name='hotel_list' ),
    path('<slug:slug>', HotelDetail.as_view(), name='hotel_detail' ),
    path('<slug:slug>/<slug:room_type_slug>', RoomTypeDetail.as_view(), name='room_type_detail' ),
] + router.urls
