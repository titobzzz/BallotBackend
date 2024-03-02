from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


from . import views


urlpatterns=[
    path('',views.RegistrationViewSet.as_view({"post":"create"}),name="registration"),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh')    
]