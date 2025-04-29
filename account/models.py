from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    melicode = models.CharField(max_length=10, null=True, blank=True)
    phone_number = PhoneNumberField(max_length=13, blank=True, null=True, unique=True)
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


    def __str__(self):
        return f'{self.username}  -  {self.phone_number}'



