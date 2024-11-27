from rest_framework import viewsets, mixins

from apps.hotel.api.serializers import HotelDetailSeriaLizer
from apps.hotel.api.serializers import HotelSeriaLizer
from apps.hotel.api.serializers import RoomTypeDetailSeriaLizer
from apps.hotel.api.serializers import RoomTypeListSeriaLizer
from apps.hotel.models import Hotel
from apps.hotel.models import RoomType


class HotelApiView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSeriaLizer

    def get_serializer_class(self):
        if self.action == "list":
            return HotelSeriaLizer
        return super().get_serializer_class()


class RoomTypeApiView(viewsets.ReadOnlyModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeListSeriaLizer

    def get_queryset(self):
        hotel_pk = self.kwargs.get("hotel_pk")
        return super().get_queryset().filter(hotel=hotel_pk)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoomTypeDetailSeriaLizer
        return super().get_serializer_class()
