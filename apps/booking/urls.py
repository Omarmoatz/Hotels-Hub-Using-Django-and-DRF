from django.urls import path

from apps.booking.views import check_avilability
from apps.booking.views import check_coupun
from apps.booking.views import checkout
from apps.booking.views import create_booking
from apps.booking.views import delete_room_from_session
from apps.booking.views import room_selection_view
from apps.booking.views import selected_rooms

app_name = "booking"

#   booking/
urlpatterns = [
    path("selected_rooms/", selected_rooms, name="selected_rooms"),
    path(
        "delete_room_from_session/",
        delete_room_from_session,
        name="delete_room_from_session",
    ),
    path("check_coupun/", check_coupun, name="check_coupun"),
    path("<slug:slug>/check_avilabilty/", check_avilability, name="check_avilabilty"),
    path("room_selection/", room_selection_view, name="room_selection"),
    path("create_booking/", create_booking, name="create_booking"),
    path("checkout/<booking_code>", checkout, name="checkout"),
]
