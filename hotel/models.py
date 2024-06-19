from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from accounts.models import User

TAG_CHOICES = (
    ("sale","sale"),
    ("new","new"),
    ("featured","featured"),
    ("cheap","cheap"),
    ("luxury","luxury"),
    ("popular","popular")
)

ICON_FEATURES = (
    ("bed","bed"),
    ("bath","bath"),
    ("wifi","wifi"),
    ("tv","tv"),
    ("fan","fan"),
    ("user-cog","Laundry"),
    ("utensils","Dinner"),
)

class Hotel(models.Model):
    user = models.ForeignKey(User, related_name='user_hotel', on_delete=models.CASCADE)
    name = models.CharField(max_length=500, default='defaul_name', blank=True, null=True)
    img = models.ImageField( upload_to='hotel/')
    description = models.TextField(max_length=5000, blank=True, null=True)
    phone = models.CharField(max_length=500, default='defaul_name', blank=True, null=True)
    address = models.CharField(max_length=500, default='defaul_name', blank=True, null=True)
    email = models.EmailField(max_length=500, default='defaul_name', blank=True, null=True)
    rating = models.PositiveIntegerField()
    tag = models.CharField( max_length=500, default='defaul_name', choices=TAG_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField( blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Hotel, self).save(*args, **kwargs) 
    

class HotelGallery(models.Model):
    Hotel = models.ForeignKey( Hotel, related_name='hotel_gallery', on_delete=models.CASCADE)
    img = models.ImageField( upload_to='hotel gallery/' )

class HotelFeatures(models.Model):
    Hotel = models.ForeignKey( Hotel, related_name='hotel_gallery', on_delete=models.CASCADE)
    icon = models.CharField( max_length=100, choices=ICON_FEATURES, blank=True, null=True)
    feature = models.CharField( max_length=500, default='defaul_name', blank=True, null=True)

class RoomType(models.Model):
    hotel = ''
    title = ''
    price = ''
    img = ''
    beds_num = ''
    room_size = ''
    created_at = ''
    slug = ''


class Room(models.Model):
    hotel = ''
    room_type = ''
    room_num = ''
    is_available = ''
    created_at = ''
    slug = ''

    def price():
        ''
    def beds_num():
        ''


class Booking(models.Model):
    user = ''
    payment_status = ''

    full_name = ''
    phone = ''
    email = ''

    hotel = ''
    room_type = ''
    room = ''
    before_discount = ''
    total = ''
    money_saved = ''
    
    check_in_date = ''
    check_out_date = ''
    total_days = ''
    num_adults = ''
    num_children = ''

    check_in = ''
    check_out = ''
    
    created_at = ''





class Review(models.Model):
    hotel = ''
    user = ''
    review = ''
    rate = ''
    created_at = ''