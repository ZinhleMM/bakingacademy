# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for the User model.
    Displays additional fields in the admin interface.
    """
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_teacher', 'profile_picture', 'bio')}),
    )
    list_display = ['username', 'email', 'is_teacher']
    list_filter = ['is_teacher'] 