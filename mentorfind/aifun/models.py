from django.db import models

class TaskRequest(models.Model):
    content = models.TextField()
