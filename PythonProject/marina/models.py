from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=1500)
