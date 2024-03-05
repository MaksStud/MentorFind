# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet


urlpatterns = [
    path('a/', AdvertisementViewSet.as_view({'post': 'create', 'get': 'list'}), name="new_advert"),
]
