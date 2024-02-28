# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet


urlpatterns = [
    path('new_advert/', AdvertisementViewSet.as_view({'post': 'create'},), name="new_advert"),
]
