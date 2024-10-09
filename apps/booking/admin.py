from django.contrib import admin

from apps.booking.models import Booking
from apps.booking.models import Coupon


@admin.register(Booking)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("user", "hotel", "full_name", "email")
    search_fields = ("hotel", "user")


admin.site.register(Coupon)
