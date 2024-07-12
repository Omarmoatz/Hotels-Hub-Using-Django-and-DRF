from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.aggregates import  Avg

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
RATE = (
    ('1',"1"),
    ('2','2'),
    ('3',"3"),
    ('4','4'),
    ('5','5')
)
class Hotel(models.Model):
    user = models.ForeignKey(User, related_name='user_hotel', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='defaul_name', blank=True, null=True)
    img = models.ImageField( upload_to='hotel/')
    subtitle = models.TextField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    min_price = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True)
    max_price = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True)
    phone = models.CharField(max_length=500, default='defaul_phone', blank=True, null=True)
    address = models.CharField(max_length=500, default='defaul_address', blank=True, null=True)
    email = models.EmailField(max_length=500, default='defaul_email', blank=True, null=True)
    # rating = models.PositiveIntegerField( blank=True, null=True)
    tag = models.CharField( max_length=500, default='defaul_name', choices=TAG_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField( blank=True, null=True)

    def avg_rating(self):
        avg = self.hotel_review.aggregate(avg_rate=Avg('rate'))
        if not avg['avg_rate']:
            result = 0
            return result
        return round(avg['avg_rate'],1) 

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Hotel, self).save(*args, **kwargs) 
    

class HotelGallery(models.Model):
    hotel = models.ForeignKey( Hotel, related_name='hotel_gallery', on_delete=models.CASCADE)
    img = models.ImageField( upload_to='hotel gallery/' )

    def __str__(self):
        return str(self.hotel)
    
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
    beds_num = models.PositiveIntegerField()    
    room_size = models.PositiveIntegerField()
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField( blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(RoomType, self).save(*args, **kwargs) 



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
        return str(self.room_type)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.room_num)
        super(Room, self).save(*args, **kwargs) 



class Review(models.Model):
    hotel = models.ForeignKey( Hotel, related_name='hotel_review', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)
    content = models.TextField( max_length=1000, blank=True, null=True)
    rate = models.CharField( max_length=50, choices=RATE)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{str(self.user)}----{self.hotel}'