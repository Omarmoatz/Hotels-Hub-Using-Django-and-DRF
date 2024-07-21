from django.urls import path

from . import views

app_name = 'booking'

  #   hotels/
urlpatterns = [
    path('selected_rooms/', views.selected_rooms, name='selected_rooms' ),
    path('<slug:slug>/check_avilabilty/', views.check_avilability, name='check_avilabilty' ),
    path('room_selection/', views.room_selection_view, name='room_selection' ),
    path('create_booking/', views.create_booking, name='create_booking' ),
]
