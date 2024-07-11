from django.urls import path

from . import views

app_name = 'hotel'

  #   hotels/
urlpatterns = [
    path('', views.HotelList.as_view(), name='hotel_list' ),
    path('<slug:slug>/', views.HotelDetail.as_view(), name='hotel_detail' ),
    path('<slug:slug>/check_avilabilty/', views.CheckAvilability.as_view(), name='check_avilabilty' ),
]
