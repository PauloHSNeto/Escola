from django.db import models
from django.db.models import Model


class Student(models.Model):
    name = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    
    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    number= models.IntegerField()
    gosto = models.CharField(max_length=10,default='bom')

    def __str__(self):
        return self.name
