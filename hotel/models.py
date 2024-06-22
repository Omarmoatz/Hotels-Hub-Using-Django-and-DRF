from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.crypto import get_random_string

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
PAYMENT_METHOD = (
    ("cach","cach"),
    ("visa","visa"),
    ("strip","strip"),
    ("paypal","paypal")
)
RATE = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
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
    hotel = models.ForeignKey( Hotel, related_name='hotel_gallery', on_delete=models.CASCADE)
    img = models.ImageField( upload_to='hotel gallery/' )

    def __str__(self):
        return str(self.Hotel)
    
class HotelFeatures(models.Model):
    hotel = models.ForeignKey( Hotel, related_name='hotel_features', on_delete=models.CASCADE)
    icon = models.CharField( max_length=100, choices=ICON_FEATURES, blank=True, null=True)
    feature = models.CharField( max_length=500, default='defaul_name', blank=True, null=True)

    def __str__(self):
        return self.feature
    
class RoomType(models.Model):
    hotel = models.ForeignKey( Hotel, related_name='hotel_room_type', on_delete=models.CASCADE)
    title = models.CharField( max_length=500, default='defaul_name', blank=True, null=True)
    price_start = models.DecimalField( max_digits=7, decimal_places=2)
    price_end = models.DecimalField( max_digits=7, decimal_places=2)
    img = models.ImageField( upload_to='room type/' )
    beds_num = models.PositiveIntegerField()    
    room_size = models.PositiveIntegerField()
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField( blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Hotel, self).save(*args, **kwargs) 



class Room(models.Model):
    hotel = models.ForeignKey( Hotel, related_name='hotel_room', on_delete=models.CASCADE)
    room_type = models.ForeignKey( RoomType, related_name='room_type', on_delete=models.CASCADE)
    room_num = models.PositiveIntegerField()
    view = models.CharField( max_length=500, default='defaul_view', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField( blank=True, null=True)

    def price(self):
        self.room_type.price

    def beds_num(self):
        self.room_type.beds_num

    def __str__(self):
        return self.room_num
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.room_num)
        super(Hotel, self).save(*args, **kwargs) 

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='booked_user', on_delete=models.CASCADE)
    payment_status = models.CharField( max_length=50, choices=PAYMENT_METHOD)

    full_name = models.CharField( max_length=500, blank=True, null=True)
    phone = models.CharField( max_length=500, blank=True, null=True)
    email = models.EmailField( max_length=900, blank=True, null=True)

    hotel = models.ForeignKey( Hotel, related_name='hotel_booked', on_delete=models.CASCADE)
    room_type = models.ForeignKey( RoomType, related_name='booked_room_type', on_delete=models.CASCADE)
    room =  models.ForeignKey( Room, related_name='booked_room', on_delete=models.CASCADE)
    before_discount = models.DecimalField( max_digits=9, decimal_places=2, blank=True, null=True)
    total = models.DecimalField( max_digits=9, decimal_places=2, blank=True, null=True)
    money_saved = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True)
    
    check_in_date = models.DateField( default=timezone.now, blank=True, null=True)
    check_out_date = models.DateField( default=timezone.now, blank=True, null=True)
    total_days = models.PositiveIntegerField(blank=True, null=True)
    num_adults = models.PositiveIntegerField(blank=True, null=True)
    num_children = models.PositiveIntegerField(blank=True, null=True)

    check_in = models.BooleanField(default=False)
    check_out = models.BooleanField(default=False)
    
    created_at = models.DateTimeField( default=timezone.now, blank=True, null=True)
    booking_code = models.CharField( max_length=500, default=get_random_string(10), blank=True, null=True)



class Review(models.Model):
    hotel = models.ForeignKey( Hotel, related_name='hotel_review', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)
    content = models.TextField( max_length=1000, blank=True, null=True)
    rate = models.CharField( max_length=50, choices=RATE)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)