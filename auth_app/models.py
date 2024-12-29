# auth/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Set email as unique

    # Additional fields
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, unique=True)
    organization = models.CharField(max_length=255, unique=True)

    # Use email as the USERNAME_FIELD for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile', 'organization']  # Other required fields

    def __str__(self):
        return self.email
