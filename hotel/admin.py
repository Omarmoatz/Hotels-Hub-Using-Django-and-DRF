from django.contrib import admin

from . import models

class HotelGalleryTabular(admin.TabularInline):
    model = models.HotelGallery

class HotelFeaturesInline(admin.TabularInline):
    model = models.HotelFeatures

class RoomTypeInline(admin.TabularInline):
    model = models.RoomType
    
class RoomsInline(admin.TabularInline):
    model = models.Room
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelGalleryTabular, HotelFeaturesInline, RoomTypeInline, RoomsInline]
    list_display = ['name', 'min_price', 'address', 'user']
    list_filter = ['name', 'min_price']
    search_fields = ['name', 'min_price']


admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.Booking)
admin.site.register(models.Review)
