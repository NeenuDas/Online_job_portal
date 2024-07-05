from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
        

    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
    )

    COUNTRY_CHOICES = (
            ('IN', 'india'),
    )

    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    short_bio = models.TextField(max_length=500, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES)
    country = models.CharField(max_length=50, default='IN', choices=COUNTRY_CHOICES)
    open_to_hiring = models.BooleanField(default=False)
    
