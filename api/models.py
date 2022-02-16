from django.db import models
from rest_framework.response import Response

# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=254)
    photo = models.ImageField(upload_to='user_photos',blank=True)
    email = models.EmailField(max_length=254,blank=True)
    ph_no = models.CharField(max_length=15,blank=True)
    team_id = models.ManyToManyField(Teams,blank=True)

    def __str__(self):
        return self.name
