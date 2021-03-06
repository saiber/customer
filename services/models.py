from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ride(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    accept = models.BooleanField(default=False)
    driver = models.ForeignKey(User, related_name='driver')
    customer = models.ForeignKey(User, related_name='customer')


class gcm_user_id(models.Model):
    username = models.CharField(max_length=80)
    gcm_id = models.TextField()