
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementView


urlpatterns = [
    path('add_announcement/', AdvertisementView.as_view(), name='add_announcement'),
]