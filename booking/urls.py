from django.urls import path

from . import views

app_name = 'booking'

  #   hotels/
urlpatterns = [
    path('<slug:slug>/check_avilabilty/', views.CheckAvilability.as_view(), name='check_avilabilty' ),
]
