from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """Admin interface for CustomUser with modern grouping and security best practices."""

    model = CustomUser

    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups')
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)

    fieldsets = (
        (_('Login Credentials'), {'fields': ('username', 'password')}),
        (_('Personal Information'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'address')}),
        (_('Permissions & Roles'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (_('Basic Information'), {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'phone',
                'address',
                'password1',
                'password2',
                'is_active',
                'is_staff',
            ),
        }),
    )
