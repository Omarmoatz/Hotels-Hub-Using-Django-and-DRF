from rest_framework import viewsets, mixins

from apps.booking.models import Booking
from apps.booking.api.serializers import BookingRetrieveSerializer


class BookingViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Booking.objects.all()
    serializer_class = BookingRetrieveSerializer

    def get_queryset(self):
        user=self.request.user
        if user.is_staff or user.is_superuser:
            return super().get_queryset()
        
        if user.user_type == user.UserType.USER:
            return super().get_queryset().filter(user=user)
        
        if user.user_type == user.UserType.SELLER:
            return super().get_queryset().filter(hotel__user=user)
        

        
        