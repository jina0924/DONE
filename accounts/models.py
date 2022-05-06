from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    image = models.ImageField(upload_to='images/', default='images/sample.jpg')
