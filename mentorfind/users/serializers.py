from rest_framework import serializers
from .models import CustomUser
from django.core.validators import MinLengthValidator, EmailValidator
from rest_framework.validators import UniqueValidator
from .validators import uppercase_letter_validation


class CustomUserSerializerLogin(serializers.ModelSerializer):
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
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserSerializerRegister(serializers.ModelSerializer):
    """
        Serializer for the CustomUser model
    """
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=CustomUser.objects.all())
        ]
    )

    email = serializers.CharField(
        validators=[
            UniqueValidator(queryset=CustomUser.objects.all()),
            EmailValidator()
        ]
    )

    password = serializers.CharField(
        validators=[
            MinLengthValidator(8),
        ]
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}