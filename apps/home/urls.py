from django.urls import path

from apps.home.views import home_view

app_name = "home"

urlpatterns = [
    path("", home_view, name="main"),
]
