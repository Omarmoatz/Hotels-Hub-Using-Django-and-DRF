from django.urls import path

from . import views

app_name = 'hotel'

  #   hotels/
urlpatterns = [
    path('', views.HotelList.as_view(), name='hotel_list' ),
    path('selected_rooms/', views.selected_rooms, name='selected_rooms' ),
    path('<slug:slug>/', views.HotelDetail.as_view(), name='hotel_detail' ),
    path('<slug:slug>/<slug:room_type_slug>/', views.RoomTypeDetail.as_view(), name='room_type_detail' ),
]
