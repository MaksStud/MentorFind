from django.db import models
from django.conf import settings
from advert.models import Advertisement

class Appointment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_appointments')
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mentor_appointments')
    advert = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    text = models.TextField()

