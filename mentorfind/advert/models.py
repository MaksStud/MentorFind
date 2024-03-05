from django.db import models
from django.conf import settings

class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='image/', null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, default=None)
    type_of_lesson = models.BooleanField(default=None)

    def __str__(self):
        return self.title
