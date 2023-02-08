from django.db import models

# Create your models here.

class Staff(models.Model):
    first=models.CharField(max_length=100,verbose_name="Enter First Name")
    last=models.CharField(max_length=100,verbose_name="Enter Last Name")
    mail=models.EmailField(verbose_name="G-Mail")
    exp=models.IntegerField(verbose_name="Experience")
    username=models.CharField(max_length=100,verbose_name="Username")
    password=models.CharField(max_length=100,verbose_name="Password")
    pic=models.ImageField(upload_to="profile_pic",null=True)
    
    def __str__(self):
        return self.first