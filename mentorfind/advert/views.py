from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Advertisement, Review
from .serializers import AdvertisementSerializer, ReviewSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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

    def list(self, request, *args, **kwargs):
        '''GET requests to the path /advert/adding-and-searching/?p=query&t=query,
        where "query" is a search query, the t c l d p notation is a search parameter,
        they can be omitted and placed in any order search, they can be omitted and
        placed in any order'''
        queryset = self.filter_queryset(self.get_queryset())

        query_params = {
            'title__icontains': self.request.query_params.get('t', None),
            'category__icontains': self.request.query_params.get('c', None),
            'location__icontains': self.request.query_params.get('l', None),
            'description__icontains': self.request.query_params.get('d', None),
            'price__gte': self.request.query_params.get('p-gte', None), # >=
            'price__lte': self.request.query_params.get('св ', None) # <=
        }

        for field, value in query_params.items():
            if value:
                queryset = queryset.filter(**{field: value})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save()
            if review:
                review.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        query_params = {
            'author': self.request.query_params.get('a', None),
            'rating__lte': self.request.query_params.get('r-lte', None),
            'rating__gte': self.request.query_params.get('r-gte', None)
        }

        for field, value in query_params.items():
            if value:
                queryset = queryset.filter(**{field: value})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

