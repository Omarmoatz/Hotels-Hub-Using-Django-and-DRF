from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HotelList, HotelDetail, RoomTypeDetail
from .api import HotelApiView

app_name = 'hotel'

router = DefaultRouter()
router.register('api', HotelApiView, basename='hotel')

  #   hotels/
urlpatterns = [
    path('', HotelList.as_view(), name='hotel_list' ),
    path('<slug:slug>', HotelDetail.as_view(), name='hotel_detail' ),
    path('<slug:slug>/<slug:room_type_slug>', RoomTypeDetail.as_view(), name='room_type_detail' ),
] + router.urls
