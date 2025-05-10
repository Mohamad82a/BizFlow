from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

class Department(models.Model):
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.department

class Role(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='roles')
    role = models.CharField(max_length=100)
    responsibility = models.CharField(max_length=255)
    def __str__(self):
        return self.role


class User(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    melicode = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)
    active = models.BooleanField(default=True)

    last_login = models.DateTimeField(null=True, blank=True)
    last_logout = models.DateTimeField(null=True, blank=True)

    def set_last_login(self):
        self.last_login = timezone.now()
        self.save(update_fields=['last_login'])

    def set_last_logout(self):
        self.last_logout = timezone.now()
        self.save(update_fields=['last_logout'])

    def save(self, *args, **kwargs):
        self.department = self.role.department
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.username}  -  {self.phone_number}'



