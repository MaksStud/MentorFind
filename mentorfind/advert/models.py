from django.db import models
from django.conf import settings

class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, default=None)
    type_of_lesson = models.BooleanField(default=None)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=None)  # rating from 1 to 5
    def __str__(self):
        return f"Review for {self.advertisement.title} by {self.author}"
