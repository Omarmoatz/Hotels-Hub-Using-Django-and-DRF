from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import HotelSeriaLizer
from .models import Hotel


@api_view(['GET'])
def hotel_list(request):
    hotel = Hotel.objects.all()
    serializer = HotelSeriaLizer(hotel, many=True).data

    return Response({'data':serializer}) 


