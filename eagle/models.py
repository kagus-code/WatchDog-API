from django.db import models
from django.contrib.auth.models import AbstractUser

class NeighbourHood(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  Occupants_count=models.PositiveSmallIntegerField()
  
