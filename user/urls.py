from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . views import UserCreateAPIView


router = routers.DefaultRouter()

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register')
]