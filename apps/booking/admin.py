from django.contrib import admin

from apps.booking.models import Booking,Coupon

@admin.register(Booking)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'full_name')
    search_fields = ('hotel', 'user')

admin.site.register(Coupon)
