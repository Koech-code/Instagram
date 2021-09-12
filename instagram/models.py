
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    photo=models.ImageField(upload_to='images')
    bio=models.TextField(max_length=1200)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='user')
    following=models.ManyToManyField(User, related_name='following')
    followers=models.ManyToManyField(User, related_name='followers')


class Image(models.Model):
    image=models.ImageField(upload_to='images')
    name=models.CharField(max_length=30)
    caption=models.CharField(max_length=30)
    profile=models.ForeignKey(Profile, on_delete=CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.TextField(max_length=500)