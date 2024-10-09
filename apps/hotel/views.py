from django.shortcuts import get_object_or_404
from django.views import generic

from apps.hotel.models import Hotel
from apps.hotel.models import HotelGallery
from apps.hotel.models import Review
from apps.hotel.models import Room
from apps.hotel.models import RoomType

# from utils import random_numbers


class HotelList(generic.ListView):
    model = Hotel
    paginate_by = 7


class HotelDetail(generic.DetailView):
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hotel_gallery"] = HotelGallery.objects.filter(hotel=self.get_object())
        context["room_type"] = RoomType.objects.filter(hotel=self.get_object())
        context["review"] = Review.objects.filter(hotel=self.get_object())
        context["related_hotels"] = Hotel.objects.all()[:6]
        context["user"] = self.request.user
        # context['related_hotels'] = Hotel.objects.all()[:random_numbers]
        return context


class RoomTypeDetail(generic.DetailView):
    model = RoomType
    context_object_name = "room_type"

    def get_object(self):
        hotel_slug = self.kwargs.get("slug")
        room_type_slug = self.kwargs.get("room_type_slug")
        return get_object_or_404(RoomType, hotel__slug=hotel_slug, slug=room_type_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.filter(
            room_type=self.get_object(),
            is_available=True,
        )
        context["name"] = self.request.GET["name"]
        context["email"] = self.request.GET["email"]
        context["checkin"] = self.request.GET["checkin"]
        context["checkout"] = self.request.GET["checkout"]
        context["adults"] = self.request.GET["adults"]
        context["children"] = self.request.GET["children"]
        return context
