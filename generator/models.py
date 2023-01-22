from django.db import models


# Create your models here.
class user_master(models.Model):
    username = models.CharField(max_length=15, null=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50)
    mobileno = models.CharField(max_length=12)
    password = models.CharField(max_length=256, null=True)
    
    # below types, this is for referance
    # img = models.ImageField(upload_to='path_to_upoad') ### towork with images you have to install library called 'pillow'
    # desc = models.TextField()
    # price = models.IntegerField
    # offer = models.BooleanField(default=False)