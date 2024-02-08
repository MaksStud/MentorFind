from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    """
        Custom user class to create and save users in database. 
        All atributes are standart Django attributes, but with additional attribute "role"
    """

    ROLE_CHOICES = [
        ("tutor", 'Tutor'),
        ("student", 'Student'),
    ]
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)