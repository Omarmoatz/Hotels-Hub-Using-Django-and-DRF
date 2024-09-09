from django.contrib import admin
from .models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'verified', 'created_at']
    list_filter = ['country', 'verified', 'created_at']

admin.site.register(User, ProfileAdmin)