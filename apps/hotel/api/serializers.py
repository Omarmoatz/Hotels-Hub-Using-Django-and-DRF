from rest_framework.reverse import reverse
from rest_framework import serializers

from apps.hotel.models import Hotel, HotelFeatures, HotelGallery, Room, RoomType
from apps.users.api.serializers import UserSerializer


class HotelGallerySeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = HotelGallery
        fields = '__all__'


class HotelFeaturesSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = HotelFeatures
        fields = ('id','feature')

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
                    'id',
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

class RoomTypeListSeriaLizer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField()
    class Meta:
        model = RoomType
        fields = '__all__'

    

class RoomTypeDetailSeriaLizer(serializers.ModelSerializer):
    hotel = HotelSeriaLizer()
    rooms = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = RoomType
        fields = '__all__'

    def get_rooms(self, obj):
        rooms = Room.objects.filter(room_type=obj)
        return RoomSeriaLizer(rooms, many=True).data

class HotelDetailSeriaLizer(serializers.ModelSerializer):
    feature = serializers.PrimaryKeyRelatedField(queryset=HotelFeatures.objects.all() ,many=True)
    # room_type = serializers.SerializerMethodField(read_only=True)
    rooms_type = RoomTypeListSeriaLizer(source='hotel_room_type', many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Hotel
        fields = '__all__'

    def get_room_type(self, obj):
        room_type = RoomType.objects.filter(hotel=obj)
        return RoomTypeListSeriaLizer(room_type, many=True).data
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)