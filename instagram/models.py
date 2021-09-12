
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    photo=models.ImageField(upload_to='images')
    bio=models.TextField(max_length=1200)
    

class Following(models.Model):
    username = models.CharField(blank=True,max_length = 255)
    followed = models.CharField(blank=True,max_length = 255)

    def __str__(self):
        return f'{self.username}'
        
class Image(models.Model):
    image=models.ImageField(upload_to='images')
    name=models.CharField(max_length=30)
    caption=models.CharField(max_length=30)
    profile=models.ForeignKey(Profile, on_delete=CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.TextField(max_length=500)