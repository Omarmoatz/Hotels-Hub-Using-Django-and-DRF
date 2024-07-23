from django.urls import path

from . import views

app_name = 'booking'

  #   booking/
urlpatterns = [
    path('selected_rooms/', views.selected_rooms, name='selected_rooms' ),
    path('delete_room_from_session/', views.delete_room_from_session, name='delete_room_from_session' ),
    path('<slug:slug>/check_avilabilty/', views.check_avilability, name='check_avilabilty' ),
    path('room_selection/', views.room_selection_view, name='room_selection' ),
    path('create_booking/', views.create_booking, name='create_booking' ),
    path('checkout/<booking_code>', views.checkout, name='checkout' ),
]
