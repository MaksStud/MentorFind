from django.db import models

from django.db import models

class WebRTCSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
