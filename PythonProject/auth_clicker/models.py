from django.db import models

class UserData(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=100)

class Note(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=1500)