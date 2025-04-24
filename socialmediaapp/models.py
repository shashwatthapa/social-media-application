from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profilepic(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='images/')

   