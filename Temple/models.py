from django.db import models
from django.db import models

# Create your models here.

class TemplesData(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    history=models.CharField(max_length=10000)
    darshtim=models.CharField(max_length=1000)
    puja=models.CharField(max_length=1000)
    food=models.CharField(max_length=1000)
    income=models.CharField(max_length=1000)

class States(models.Model):
    long=models.FloatField()
    lat=models.FloatField()

