from rest_framework import generics
from rest_framework.response import Response

from .serializers import HotelSeriaLizer,HotelDetailSeriaLizer
from .models import Hotel


class HotelApiView(generics.GenericAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSeriaLizer

    def get(self, request, *args, **kwargs):
        # generics.ListAPIView
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

