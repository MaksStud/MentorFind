from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required=True,
    )
    class Meta:
        model = Advertisement
        fields = ('title', 'description', 'price', 'author')
