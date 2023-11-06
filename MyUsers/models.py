from django.db import models

from django.contrib.auth.models import AbstractBaseUser

from .manager import UserManager

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=250)
    email = models.EmailField(blank=False, unique=True)
    bio = models.TextField(null=True)
    objects = UserManager()

    USERNAME_FIELD= 'email'
    def __str__(self) -> str:
        return f"the  current user is {self.name}"