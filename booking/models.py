from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta

from accounts.models import User
from hotel.models import Hotel, Room, RoomType


PAYMENT_METHOD = (
    ("cach","cach"),
    ("visa","visa"),
    ("strip","strip"),
    ("paypal","paypal")
)

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='booked_user', on_delete=models.CASCADE)
    payment_method = models.CharField( max_length=50, choices=PAYMENT_METHOD, blank=True, null=True)

    full_name = models.CharField( max_length=500, blank=True, null=True)
    phone = models.CharField( max_length=500, blank=True, null=True)
    email = models.EmailField( max_length=900, blank=True, null=True)

    hotel = models.ForeignKey( Hotel, related_name='hotel_booked', on_delete=models.CASCADE)
    room_type = models.ManyToManyField( RoomType )
    room =  models.ManyToManyField( Room )
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
    booking_code = models.CharField( max_length=500, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{str(self.user)}----{self.hotel}----{self.full_name}---{self.booking_code}'
    
    def save(self, *args, **kwargs):
       self.booking_code = get_random_string(10)
       super().save(*args, **kwargs) 
    

class Coupon(models.Model):
    code = models.CharField( max_length=100, blank=True, null=True)
    discount = models.PositiveIntegerField( blank=True, null=True)
    quantity = models.PositiveIntegerField( blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField( blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.discount}% off"
    
    def save(self, *args, **kwargs):
       week = timedelta(days=7)
       self.end_date = self.start_date + week
       super(Coupon, self).save(*args, **kwargs) 
