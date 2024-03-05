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

    def list(self, request, *args, **kwargs):
        '''GET-запити на шлях /advert/a/?p=запит&t=запит, де "запит"
        є пошуковим запитом, познчання t c l d p є параментрами для
        пошуку їх можна не передавати і розміщувати в любому порядку'''
        queryset = self.filter_queryset(self.get_queryset())
        title_query = self.request.query_params.get('t', None)
        category_query = self.request.query_params.get('c', None)
        location_query = self.request.query_params.get('l', None)
        description_query = self.request.query_params.get('d', None)
        price_query = self.request.query_params.get('p', None)

        if title_query:
            queryset = queryset.filter(title__icontains=title_query)
        if category_query:
            queryset = queryset.filter(category__icontains=category_query)
        if location_query:
            queryset = queryset.filter(location__icontains=location_query)
        if description_query:
            queryset = queryset.filter(description__icontains=description_query)
        if price_query:
            queryset = queryset.filter(price__icontains=price_query)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


