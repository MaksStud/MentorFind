# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet, ReviewViewSet, AdvertisementGetByIdViewSet


urlpatterns = [
    path('adding-and-searching/', AdvertisementViewSet.as_view({'post': 'create', 'get': 'list'}), name='adding-and-searching'),
    path('review/', ReviewViewSet.as_view({'post': 'create', 'get': 'list'}), name='review'),
    path('getById/<int:pk>/', AdvertisementGetByIdViewSet.as_view({'get': 'retrieve'}), name='getById'),

]
