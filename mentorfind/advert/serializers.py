from rest_framework import serializers
from .models import Advertisement, Review
from django.db.models import Avg


class AdvertisementSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    title = serializers.CharField(required=True)

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'category', 'price', 'description', 'image', 'author', 'location', 'type_of_lesson', 'average_rating']
        read_only_fields = ['id', 'average_rating']

    def get_average_rating(self, obj):
        return obj.review_set.aggregate(Avg('rating'))['rating__avg']


class AdvertisementSerializerEdit(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    image = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    type_of_lesson = serializers.CharField(required=False)

    class Meta:
        model = Advertisement
        fields = ['title', 'category', 'price', 'description', 'image', 'location', 'type_of_lesson']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'rating', 'advertisement', 'author')