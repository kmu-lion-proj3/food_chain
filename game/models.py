from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.
class Animal(models.Model):
    kind=models.CharField(max_length=200)
    status=models.IntegerField()
    victory=models.BooleanField(default=True)
    location=models.CharField(max_length=200)
    limited_location=models.CharField(max_length=200, null=True)
    life=models.BooleanField(default=True)
    ID=models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    victory_condition=models.TextField(null=True)
    defeat_condition=models.TextField(null=True)
    uniq=models.TextField(null=True)
    starve=models.IntegerField(default=10)
    def __str__(self):
        return self.kind
    def id_update(self, user):
        self.ID = user
        self.save()
    def location_update(self, location):
        self.location = location
        self.save()

class Situation(models.Model):
    attacker = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="attacker")
    attacked = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="attacked")
    location = models.CharField(max_length=200)
    round = models.IntegerField()
    def __str__(self):
        round = self.round
        location = self.location
        return str(str(round)+'round - place : '+ str(location))

class Flag(models.Model):
    flag = models.BooleanField()