from django.db import models


class Hotel(models.Model):
    name = ''
    img = ''
    description = ''
    phone = ''
    address = ''
    email = ''
    rating = ''
    slug = ''
    created_at = ''
    tag = ''' sale - new - hot - top - featured - special - popular - 
            best - offer - discount - cheap - luxury - deal - budget - unique 
            - trend - exclusive - amazing - great - super'''

    

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
    slug = ''
    created_at = ''



class Review(models.Model):
    hotel = ''
    user = ''
    review = ''
    rate = ''
    created_at = ''