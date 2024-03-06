from rest_framework import serializers
from .models import Advertisement, Review


class AdvertisementSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required=True,
    )

    class Meta:
        model = Advertisement
        fields = ('title', 'category', 'description', 'price', 'image', 'author', 'location', 'type_of_lesson')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'rating', 'advertisement', 'author')