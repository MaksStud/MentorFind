from rest_framework import serializers
from .models import Message
from users.serializers import CustomUserSerializerRead

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'receiver', 'sender', 'text']


class MessageListSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializerRead()
    class Meta:
        model = Message
        fields = ['id', 'receiver', 'sender', 'text']