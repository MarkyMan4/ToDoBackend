from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            'id',
            'name',
            'description',
            'start_date',
            'end_date',
            'completed',
            'date_completed'
        ]
