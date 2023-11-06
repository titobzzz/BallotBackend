from typing import Any
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
         """
        creates and saves a user with input arguments
        """
         
         if not email:
              raise ValueError("User must have email")
         user = self.model(
              email= self.normalize_email(email),
              username=extra_fields["username"]
         )
         user.set_password(password)
         user.save()
         return user
    
    def create_superuser(self, email, password=None, **extra_fields):
         
        """
        creates the super user
        """
        extra_fields.setdefault(is_active=True)
        extra_fields.setdefault(is_staff=True)
        extra_fields.setdefault(is_superuser=True)