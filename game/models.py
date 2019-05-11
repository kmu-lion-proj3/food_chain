from django.db import models

# Create your models here.
class Animal(models.Model):
    kind=models.CharField(max_length=200)
    status=models.IntegerField()
    victory=models.BooleanField(default=True)
    location=models.CharField(max_length=200)
    limited_location=models.CharField(max_length=200)
    life=models.BooleanField(default=True)
