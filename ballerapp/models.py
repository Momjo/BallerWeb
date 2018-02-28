import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms


class Adresse(models.Model):
    country = models.CharField(max_length=20,)
    city = models.CharField(max_length=20,)
    street = models.CharField(max_length=20,)
    hous_number = models.CharField(max_length=15,)
    place_pic = models.FileField(upload_to='place_pic', blank=True)
    #pub_date = models.DateTimeField('date published', null=True)

    #def was_published_recently(self):
    #   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
     #   add the id for users id
    def __str__(self):
        return self.city


# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     website = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_images', blank=True)
#     def __str__(self):
#         return self.user.username


# class Profile(models.Model):
#     user =models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length = 30, blank = True )
#     birth_date = models.DateField(null = True, blank = True)
