from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models

class HotelGalleryTabular(admin.TabularInline):
    model = models.HotelGallery
class HotelFeaturesInline(admin.TabularInline):
    model = models.HotelFeatures
class RoomTypeInline(admin.TabularInline):
    model = models.RoomType

class RoomsInline(admin.TabularInline):
    model = models.Room
class RivewInline(admin.TabularInline):
    model = models.Review
class HotelAdmin(SummernoteModelAdmin):
    inlines = [HotelGalleryTabular, HotelFeaturesInline, RoomTypeInline, RoomsInline, RivewInline]
    list_display = ('name', 'min_price', 'address', 'user')
    list_filter = ('name', 'min_price')
    search_fields = ('name', 'min_price')
    summernote_fields = ('description', )


admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.Booking)
