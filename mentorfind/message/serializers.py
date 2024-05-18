from rest_framework import serializers
from .models import Message
from users.serializers import CustomUserSerializerRead

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'teacher', 'student', 'text']


class MessageListSerializer(serializers.ModelSerializer):
    student = CustomUserSerializerRead()
    class Meta:
        model = Message
        fields = ['id', 'teacher', 'student', 'text']