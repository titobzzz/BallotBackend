from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import permissions
from .models import *
from .serializer import *



class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User
    serializer_class = [UserRegistrationSerializer]