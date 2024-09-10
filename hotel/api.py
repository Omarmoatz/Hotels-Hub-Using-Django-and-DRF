from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import HotelSeriaLizer,HotelDetailSeriaLizer
from .models import Hotel


class HotelApiView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSeriaLizer
    lookup_field = 'slug'

    # def get(self, request, *args, **kwargs):
    #     # generics.ListAPIView
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    

