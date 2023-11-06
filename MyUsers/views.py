from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models  import User

from .serializer import UserRegistration

from django.shortcuts import render

# Create your views here.

class RegistrationViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset=User.objects.all()
    serializer_class = UserRegistration
    permission_classes= [AllowAny]


Registration = RegistrationViewSet.as_view({"post":"create", "get":"retrieve"})