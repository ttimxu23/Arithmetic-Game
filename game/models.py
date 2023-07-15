from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class UserStats(models.Model):
    user_ref = models.OneToOneField(User, related_name="stats", on_delete=models.CASCADE)
    rounds_played = models.IntegerField(blank=True, null=True, default=0)
    halfmin_best = models.IntegerField(blank=True, null=True, default=0)
    onemin_best = models.IntegerField(blank=True, null=True, default=0)
    twomin_best = models.IntegerField(blank=True, null=True, default=0)
    fivemin_best = models.IntegerField(blank=True, null=True, default=0)
    tenmin_best = models.IntegerField(blank=True, null=True, default=0)


