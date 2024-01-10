from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'',views.BallotView,basename="Ballots")

urlpatterns =[
    path('',include(router.urls),name="Ballots")
]