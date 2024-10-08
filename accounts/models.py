from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager, AbstractUser
import uuid

from .manager import UserManager

# Create your models here.


class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)
    username = models.CharField(max_length=250,blank=False)
    full_name=models.CharField(max_length=250, default="Anonymous", null=True)
    avatar = models.ImageField(upload_to="MyUser/profile_pictures",default="static/Images/Avatar.jpg")
    email = models.EmailField(blank=False, unique=True)
    date_of_birth=models.DateField(null=True)
    bio = models.TextField(null=True)
    objects = UserManager()

    USERNAME_FIELD= 'email'
    def __str__(self) -> str:
        return f"the  current user is {self.username}"
