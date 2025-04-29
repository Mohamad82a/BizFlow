from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone_number', 'first_name', 'last_name', 'email', 'last_login','last_logout', 'active',)
    list_filter = ('username', 'phone_number', 'first_name', 'last_name', 'email',)
