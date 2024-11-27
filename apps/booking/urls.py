from django.urls import path

from apps.booking.views import (
    check_avilability,
    check_coupun,
    checkout,
    create_booking,
    delete_room_from_session,
    room_selection_view,
    selected_rooms,
    success_payment,
    BookingListView,
)
#   booking/
urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='bookings_list'),

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
    path("success/<booking_id>/", success_payment, name="success_payment"),
]

app_name = "booking"
