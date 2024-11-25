from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    drivers_license_number = models.CharField(max_length=100, blank=True, null=True)
    license_expiry_date = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bookings_count = models.IntegerField(default=0)
    preferred_car_type = models.CharField(max_length=50, blank=True, null=True)
    preferred_pickup_location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
