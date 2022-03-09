from django.db import models
# from django.contrib.auth import AbstractUser , BaseUserManager
import uuid
# Create your models here.
class CustomerUser(models.Model):
    username = models.CharField(max_length=255 , unique=True)
    email = models.EmailField(max_length=255 , unique= True)
    password = models.CharField(max_length=255)
    jwt = models.CharField(max_length=200)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

