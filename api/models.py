from django.db import models

# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    ph_no = models.CharField(max_length=10)
    team_id = models.ManyToManyField(Teams)

    def __str__(self):
        return self.name
