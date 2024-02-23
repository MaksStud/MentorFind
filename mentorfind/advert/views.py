# views.py
from rest_framework import status
from rest_framework import viewsets
from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.response import Response

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            advert = serializer.save()
            if advert:
                advert.save()

                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

