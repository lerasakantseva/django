from django.db import models
from django.contrib.auth.models import import User

class Core(models.Model):
    user = models.OneToOneField(User, null = False, on_delete=models.Cascade)
    coins = models.IntegerField(default = 0)
    click_power = models.IntegerField(default=1)