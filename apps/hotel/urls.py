from django.urls import path

from apps.hotel.views import HotelList, HotelDetail, RoomTypeDetail

#   hotels/
urlpatterns = [
    path("", HotelList.as_view(), name="hotel_list"),
    path("<slug:slug>", HotelDetail.as_view(), name="hotel_detail"),
    path(
        "<slug:slug>/<slug:room_type_slug>",
        RoomTypeDetail.as_view(),
        name="room_type_detail",
    ),
]

app_name = "hotel"
