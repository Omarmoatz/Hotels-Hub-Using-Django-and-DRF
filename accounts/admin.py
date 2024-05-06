from django.contrib import admin
from .models import User,Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'verified', 'created_at']
    list_filter = ['country', 'verified', 'created_at']

admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)