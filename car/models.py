from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    purchaser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    model = models.CharField(max_length=255,default='Add car model ')
    images = models.TextField(default='Add car image')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_DetailView',args=[self.id])
