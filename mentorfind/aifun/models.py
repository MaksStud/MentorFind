from django.db import models
from django.contrib.postgres.fields import ArrayField

class TextGeneration(models.Model):
    content = models.TextField()

class ImageGeneration(models.Model):
    content = ArrayField(models.CharField(max_length=100), blank=True)
