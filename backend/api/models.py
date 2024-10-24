from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    user_id = models.CharField(unique=True, max_length=26, null=False)
    password = models.CharField(null=False, blank=False, max_length=16)
    # username = models.CharField(null=False, blank=True, unique=False,max_length=16)


    def save(self,*args, **kwargs):
        if not self.password.startswith('pbkd'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
              
        
