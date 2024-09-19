from rest_framework import generics, viewsets
from rest_framework.response import Response

from apps.hotel.api.serializers import HotelSeriaLizer,HotelDetailSeriaLizer, RoomTypeListSeriaLizer, RoomTypeDetailSeriaLizer
from apps.hotel.models import Hotel, RoomType


class HotelApiView(viewsets.ModelViewSet): 
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSeriaLizer
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return HotelSeriaLizer
        return super().get_serializer_class()

class RoomTypeApiView(viewsets.ReadOnlyModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeListSeriaLizer

    def get_queryset(self):
        hotel_pk = self.kwargs.get('hotel_pk')
        return super().get_queryset().filter(hotel=hotel_pk)
         
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RoomTypeDetailSeriaLizer
        return super().get_serializer_class()