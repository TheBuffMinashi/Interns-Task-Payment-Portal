from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ('Personal Information', {
         'fields': ('email', 'full_name', 'password')}),
        ("Permissions",
            {'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        ('Personal Information', {
            'classes': ('wide',),
            'fields': (
                'email', 'full_name', 'password1', 'password2',
            )}),
        ('Permissions', {
            'classes': ('wide',),
            'fields':
            ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')})
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
