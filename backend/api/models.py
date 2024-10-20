from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    user_id = models.CharField(unique=True, blank=False, max_length=16)
    password = models.CharField(blank=False, max_length=21)
    



