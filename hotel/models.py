from django.db import models


class Hotel(models.Model):
    user = ''
    name = ''
    img = ''
    description = ''
    phone = ''
    address = ''
    email = ''
    rating = ''
    tag = ''' sale - new - hot - top - featured - special - popular - 
        best - offer - discount - cheap - luxury - deal - budget - unique 
        - trend - exclusive - amazing - great - super'''
    created_at = ''
    slug = ''

    

class HotelGallery(models.Model):
    Hotel = ''
    img = ''


class HotelFeatures(models.Model):
    Hotel = ''
    icon = ''
    feature = ''

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