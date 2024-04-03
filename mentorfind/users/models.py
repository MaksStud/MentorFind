from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#class Roles(models.Model):
#   name = models.CharField(max_length=20)
#    def __str__(self):
#        return self.name

class CustomUser(AbstractUser):
    """
        Custom user class to create and save users in database. 
        All atributes are standart Django attributes, but with additional attribute "role"
    """