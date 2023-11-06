from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User

class UserRegistration(ModelSerializer):
    password = serializers.Charfiled(write_only=True, style={"input_type" : "password"})

    class Meta:
        model= User
        fields=[
            "username",
            "email",
            "password"
        ]

        def create(self, registrationData):
            """
            to create user 
            """
            user = User.objects.create_user(
                email=registrationData["email"],
                username= registrationData["username"],
                password = registrationData["password"]                   
            )
            return user