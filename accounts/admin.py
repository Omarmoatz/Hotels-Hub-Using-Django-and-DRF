from django.contrib import admin
from .models import User

@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'verified', 'is_superuser', 'is_active', 'created')
    list_filter = ('country', 'verified', 'created')
    search_fields = ('email', 'username', 'country')
    readonly_fields = ('code', 'created', 'modified', 'date_joined', 'last_login')
    ordering = ('-created',)