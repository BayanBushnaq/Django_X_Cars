from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    Phone_Number= models.CharField(max_length=255, null=True,blank=True)

    def __str__(self):
        return self.username