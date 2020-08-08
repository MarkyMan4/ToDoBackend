from rest_framework import serializers
from .models import ToDo
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
