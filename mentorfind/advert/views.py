# views.py
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            advert = serializer.save()
            if advert:
                advert.save()

                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    #GET-запити на шлях advert/a/?q=запит, де "запит" є пошуковим запитом.
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter( Q(title__icontains=query) )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

