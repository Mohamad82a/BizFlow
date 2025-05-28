from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Department, Role, User, OTP


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone', 'full_name', 'email', 'last_login','last_logout', 'active',)
    list_filter = ('username', 'phone', 'full_name' , 'email', 'role', 'department')


    fieldsets = [
        ('General', {"fields": ["username", "department", "role", "password"]}),
        ("Personal Info", {"fields": ["full_name", "phone", "email"]}),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser", "groups", "user_permissions"]}),
    ]
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(OTP)

