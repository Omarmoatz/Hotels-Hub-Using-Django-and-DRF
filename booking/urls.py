from django.urls import path

from . import views

app_name = 'booking'

  #   hotels/
urlpatterns = [
    path('<slug:slug>/check_avilabilty/', views.check_avilability, name='check_avilabilty' ),
]
