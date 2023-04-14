from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'phone',
        'email',
        'first_name',
        'last_name',
        'date_joined',
        'phone_verified',
        'email_verified',
        'balance'
    )
