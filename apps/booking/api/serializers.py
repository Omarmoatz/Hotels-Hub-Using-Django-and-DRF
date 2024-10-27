from rest_framework import serializers

from apps.booking.models import Booking


class BookingRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'