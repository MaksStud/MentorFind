from rest_framework import serializers
from .models import ViewHistory
from selected.models import Selected
from advert.serializers import AdvertisementSerializer
from django.db.models import Avg


class ViewHistorySerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()
    advertisement = AdvertisementSerializer()

    class Meta:
        model = ViewHistory
        fields = ['id', 'user', 'advertisement', 'timestamp', 'average_rating', 'is_saved']

    def get_average_rating(self, obj):
        return obj.advertisement.review_set.aggregate(Avg('rating'))['rating__avg']

    def get_is_saved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Selected.objects.filter(user=request.user, advertisement=obj.advertisement).exists()
        return False

