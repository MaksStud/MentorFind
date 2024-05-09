from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
        Custom user class to create and save users in database. 
        All atributes are standart Django attributes, but with additional attribute "role"
    """
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)