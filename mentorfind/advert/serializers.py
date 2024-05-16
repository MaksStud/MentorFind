from rest_framework import serializers
from .models import Advertisement, Review
from django.db.models import Avg
from selected.models import Selected

class AdvertisementSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    title = serializers.CharField(required=True)
    is_saved = serializers.SerializerMethodField()

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'category', 'price', 'description', 'image',  'author', 'location', 'type_of_lesson', 'average_rating', 'is_saved']
        read_only_fields = ['id', 'average_rating', 'is_saved']

    def get_average_rating(self, obj):
        return obj.review_set.aggregate(Avg('rating'))['rating__avg']

    def get_is_saved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Selected.objects.filter(user=request.user, advertisement=obj).exists()
        return False


class AdvertisementSerializerGetById(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()

    class Meta:
        model = Advertisement
        fields = ['title', 'category', 'price', 'description', 'image', 'author', 'location', 'type_of_lesson', 'average_rating', 'is_saved']

    def get_average_rating(self, obj):
        return obj.review_set.aggregate(Avg('rating'))['rating__avg']

    def get_is_saved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Selected.objects.filter(user=request.user, advertisement=obj).exists()
        return False


class AdvertisementSerializerEdit(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    description = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    location = serializers.CharField(required=False)
    type_of_lesson = serializers.BooleanField(required=False)
    author = serializers.ReadOnlyField(source='author.pk')

    class Meta:
        model = Advertisement
        fields = ['title', 'category', 'price', 'description', 'image', 'location', 'type_of_lesson', 'author']


class ReviewSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('text', 'rating', 'advertisement', 'author', 'author_name')

    def get_author_name(self, obj):
        return obj.author.username if obj.author else None
