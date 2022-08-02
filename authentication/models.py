from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    created_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    fav_food = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    instructions = models.TextField(max_length=200)
    email = models.EmailField(unique=True)
