from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Department, Role, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone_number', 'first_name', 'last_name', 'email', 'last_login','last_logout', 'active',)
    list_filter = ('username', 'phone_number', 'first_name', 'last_name', 'email',)


    fieldsets = [
        ('General', {"fields": ["username", "department", "role", "password"]}),
        ("Personal Info", {"fields": ["first_name", "last_name", "phone_number", "melicode", "email"]}),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser", "groups", "user_permissions"]}),
    ]
admin.site.register(Department)
admin.site.register(Role)