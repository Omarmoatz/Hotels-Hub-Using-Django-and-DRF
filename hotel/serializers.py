from rest_framework import serializers
from .models import Hotel, HotelFeatures, HotelGallery, Room, RoomType


class HotelGallerySeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = HotelGallery
        fields = '__all__'



class HotelFeaturesSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = HotelFeatures
        fields = '__all__'


class RoomTypeSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class HotelSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'



class HotelDetailSeriaLizer(serializers.ModelSerializer):
    hotel_feature = HotelFeaturesSeriaLizer()
    class Meta:
        model = Hotel
        fields = (
                    'user',
                    'name',
                    'hotel_feature',
                    'img',
                    'subtitle',
                    'description',
                    'min_price',
                    'max_price',
                    'phone',
                    'address',
                    'email'
                   )