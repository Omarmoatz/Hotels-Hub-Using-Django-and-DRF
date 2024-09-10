from rest_framework.reverse import reverse
from rest_framework import serializers

from .models import Hotel, HotelFeatures, HotelGallery, Room, RoomType


class HotelGallerySeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = HotelGallery
        fields = '__all__'



class HotelFeaturesSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = HotelFeatures
        fields = ('feature', )


class RoomTypeSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class HotelSeriaLizer(serializers.ModelSerializer):
    # detail_url = serializers.SerializerMethodField()
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='hotel:hotel-detail',
        lookup_field = 'slug'
    )
    class Meta:
        model = Hotel
        fields = (
                    'user',
                    'name',
                    'img',
                    'min_price',
                    'max_price',
                    'phone',
                    'address',
                    'email',
                    'get_absolute_url',
                    'get_api_url',
                    'detail_url',
                   )
        
    def get_detail_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        
        return reverse('hotel:hotel-detail', kwargs={'slug':obj.slug}, request=request)



class HotelDetailSeriaLizer(serializers.ModelSerializer):
    feature = HotelFeaturesSeriaLizer(many=True)
    class Meta:
        model = Hotel
        fields = '__all__'