from rest_framework import serializers
from .models import Appointment
from users.serializers import CustomUserSerializerRead
from advert.serializers import AdvertisementSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'student', 'mentor', 'text', 'advert']


class AppointmentListSerializer(serializers.ModelSerializer):
    student = CustomUserSerializerRead()
    mentor = CustomUserSerializerRead()
    advert = AdvertisementSerializer()
    class Meta:
        model = Appointment
        fields = ['id', 'student', 'mentor', 'text', 'advert']