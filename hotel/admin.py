from django.contrib import admin

from . import models

admin.site.register(models.Hotel)
admin.site.register(models.HotelGallery)
admin.site.register(models.HotelFeatures)
admin.site.register(models.Room)
admin.site.register(models.RoomType)
admin.site.register(models.Booking)
admin.site.register(models.Review)
