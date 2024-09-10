from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpRequest

from .models import MainSettings

@admin.register(MainSettings)
class MainSettingsAdmin(admin.ModelAdmin):
    list_display = ('logo_tag', 'name', 'email', 'phone')

    def has_delete_permission(self, request, obj=None):
        # disable the delete button in the admin
        return False
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        if MainSettings.objects.exists():
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'You can not create more than one object')
            return False
        return super().has_add_permission(request)

