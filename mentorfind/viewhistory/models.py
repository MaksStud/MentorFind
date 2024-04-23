from django.db import models
from django.apps import apps
from django.conf import settings


class ViewHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advertisement = models.ForeignKey('advert.Advertisement',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
