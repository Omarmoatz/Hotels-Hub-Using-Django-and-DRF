from django.contrib import admin

from .models import MainSettings

class MainSettingsAdmin(admin.ModelAdmin):
    list_display = ('logo_tag', 'name', 'email', 'phone')

admin.site.register(MainSettings, MainSettingsAdmin)
