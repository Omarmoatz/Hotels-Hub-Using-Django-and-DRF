from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin

from apps.hotel.models import Hotel
from apps.hotel.models import HotelFeatures
from apps.hotel.models import HotelGallery
from apps.hotel.models import Review
from apps.hotel.models import Room
from apps.hotel.models import RoomType


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
    list_display = ("name", "min_price", "address", "user", "img_tag", "created")
    list_filter = ("name", "min_price")
    search_fields = ("name", "min_price")
    summernote_fields = ("description",)

    def img_tag(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style= max-width:50px; max-height:50px;" />',
            )
        return "-"


admin.site.register(HotelFeatures)
