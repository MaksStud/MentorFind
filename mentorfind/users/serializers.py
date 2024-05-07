from rest_framework import serializers
from .models import CustomUser
from django.core.validators import MinLengthValidator, EmailValidator
from rest_framework.validators import UniqueValidator
from .validators import uppercase_letter_validation
from rest_framework import serializers


class CustomUserSerializerLogin(serializers.ModelSerializer):
    """
        Serializer for the login
    """
    username = serializers.CharField(required=False, validators=[])
    password = serializers.CharField(validators=[])
    photo = serializers.ImageField(source='user_photos/', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'photo')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'Token']


class CustomUserSerializerRegister(serializers.ModelSerializer):
    """
        Serializer for the registration
    """
    username = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    email = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all()), EmailValidator()])
    password = serializers.CharField(validators=[MinLengthValidator(8), uppercase_letter_validation])
    photo = serializers.ImageField(source='user_photos/', read_only=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'photo')
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserSerializerRead(serializers.ModelSerializer):
    photo = serializers.ImageField(source='user_photos/', read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'photo']


class CustomUserSerializerEdit(serializers.ModelSerializer):
    username = serializers.CharField(required=False, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(validators=[MinLengthValidator(8), uppercase_letter_validation], required=False)
    email = serializers.CharField(required=False, validators=[UniqueValidator(queryset=CustomUser.objects.all()), EmailValidator()])
    photo = serializers.ImageField(required=False, source='user_photos/')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'photo']


class CustomUserTopSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField()
    advertisement_count = serializers.IntegerField()
    photo = serializers.ImageField(source='user_photos/', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'avg_rating', 'advertisement_count', 'photo']

