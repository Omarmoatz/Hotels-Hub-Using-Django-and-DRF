from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import HotelGallery, RoomType, Room, Hotel, HotelFeatures, Review

class HotelGalleryTabular(admin.TabularInline):
    model = HotelGallery

# class HotelFeaturesInline(admin.TabularInline):
#     model = HotelFeatures

class RoomTypeInline(admin.TabularInline):
    model = RoomType

class RoomsInline(admin.TabularInline):
    model = Room
class RivewInline(admin.TabularInline):
    model = Review

@admin.register(Hotel)
class HotelAdmin(SummernoteModelAdmin):
    inlines = [HotelGalleryTabular, RoomTypeInline, RoomsInline, RivewInline]
    list_display = ('name', 'min_price', 'address', 'user')
    list_filter = ('name', 'min_price')
    search_fields = ('name', 'min_price')
    summernote_fields = ('description', )


admin.site.register(HotelFeatures)
