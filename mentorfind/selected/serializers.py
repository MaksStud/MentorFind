from rest_framework import serializers
from .models import Selected


class SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selected
        fields = ['id', 'user', 'advertisement']