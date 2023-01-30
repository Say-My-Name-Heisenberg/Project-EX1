from django.db import models

# Create your models here.

class Staff(models.Model):
    first=models.CharField(max_length=100)
    last=models.CharField(max_length=100)
    mail=models.EmailField()
    exp=models.IntegerField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
