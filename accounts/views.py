from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, mixins, exceptions
from rest_framework import permissions
from .models import *
from .serializer import *


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
