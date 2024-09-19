from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.utils.html import format_html

from apps.home.models import MainSettings

@admin.register(MainSettings)
class MainSettingsAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'phone', 'img_tag')

    def has_delete_permission(self, request, obj=None):
        # disable the delete button in the admin
        return False
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        # disable the Create button in the admin
        if MainSettings.objects.exists():
            messages.set_level(request, messages.ERROR)
            return False
        return super().has_add_permission(request)
    
    def img_tag(self, obj):
        if obj.logo:
            return format_html(f'<img src="{obj.logo.url}" width="150" height="60"/>')
