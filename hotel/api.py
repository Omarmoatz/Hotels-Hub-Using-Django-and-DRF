from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import HotelSeriaLizer,HotelDetailSeriaLizer
from .models import Hotel


@api_view(['GET'])
def hotel_list(request):
    hotel = Hotel.objects.all()
    serializer = HotelSeriaLizer(hotel, many=True, context={'request': request}).data

    return Response({'data':serializer}) 


class HotelDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSeriaLizer
    lookup_field = 'slug'
