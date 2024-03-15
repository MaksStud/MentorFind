from rest_framework import serializers
from .models import Advertisement, Review
from django.db.models import Avg


class AdvertisementSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    title = serializers.CharField(required=True)

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'category', 'price', 'description', 'image', 'author', 'location', 'type_of_lesson', 'average_rating']

    def get_average_rating(self, obj):
        return obj.review_set.aggregate(Avg('rating'))['rating__avg']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'rating', 'advertisement', 'author')