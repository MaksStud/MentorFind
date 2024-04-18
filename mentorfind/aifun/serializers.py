from rest_framework import serializers
from .models import ImageGeneration, TextGeneration



class TextGenerationSerializer(serializers.Serializer):
    content = serializers.CharField()

    class Meta:
        model = TextGeneration
        fields = '__all__'


class ImageGenerationSerializer(serializers.Serializer):
    content = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = ImageGeneration
        fields = '__all__'
