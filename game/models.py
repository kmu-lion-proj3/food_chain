from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Animal(models.Model):
    kind=models.CharField(max_length=200)
    status=models.IntegerField()
    victory=models.BooleanField(default=True)
    location=models.CharField(max_length=200)
    limited_location=models.CharField(max_length=200, null=True)
    life=models.BooleanField(default=True)
    ID=models.OneToOneField(User,on_delete=models.CASCADE,default=True)
    def __str__(self):
        return self.kind