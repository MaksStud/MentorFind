from rest_framework import serializers
from .models import TaskRequest

class TaskRequestSerializer(serializers.Serializer):
    content = serializers.CharField()

    class Meta:
        model = TaskRequest
        fields = '__all__'
