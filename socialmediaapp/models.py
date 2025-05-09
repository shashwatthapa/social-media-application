from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profilepic(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='images/')
    

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content= models.TextField()

    def __str__(self):
        return self.title


   