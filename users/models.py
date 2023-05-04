from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class User(models.Model):    
    user_name = models.CharField(max_length = 32,blank=True,null=True ,unique=True)
    password = models.CharField(max_length = 128, blank=True,null=True)
    update_time = models.DateTimeField(auto_now=True)
    error_count = models.IntegerField(blank=True,null=True,default=-1)
