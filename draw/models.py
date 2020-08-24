from django.db import models
from accounts.models import Profile
from django.conf import settings
# Create your models here.

class Draw(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    first = models.CharField(max_length=50, blank=False)
    second = models.CharField(max_length=50, blank=False)
    third = models.CharField(max_length=50, blank=False)
    