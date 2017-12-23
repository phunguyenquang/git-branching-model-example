from django.db import models

class Device(models.Model):
    uuid = models.CharField(max_length=255, primary_key=True)
