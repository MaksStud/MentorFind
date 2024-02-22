# views.py
from rest_framework import viewsets
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
