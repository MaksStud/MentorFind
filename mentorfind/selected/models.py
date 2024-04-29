from django.db import models
from django.conf import settings


class Selected(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advertisement = models.ForeignKey('advert.Advertisement',on_delete=models.CASCADE)