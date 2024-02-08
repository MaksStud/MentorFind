from rest_framework import serializers
from .models import CustomUser
from django.core.validators import MinLengthValidator 
from rest_framework.validators import UniqueValidator
from .validators import uppercase_letter_validation

class CustomUserSerializer(serializers.ModelSerializer):
    """
        Serializer for the CustomUser model
    """
    username = serializers.CharField(
        validators=[
            MinLengthValidator(5)
        ]
    )
    password = serializers.CharField(
        validators=[
            MinLengthValidator(5), 
            uppercase_letter_validation
        ]
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}