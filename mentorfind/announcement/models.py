from django.db import models
from mentorfind.users.models import CustomUser


class Advertisement(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()