from django.urls import path
from .views import AdvertisementViewSet, ReviewViewSet, AdvertisementEditViewSet


urlpatterns = [
    path('adding-and-searching/', AdvertisementViewSet.as_view({'post': 'create', 'get': 'list'}), name='adding-and-searching'),
    path('review/', ReviewViewSet.as_view({'post': 'create', 'get': 'list'}), name='review'),
    path('edit/<int:pk>/', AdvertisementEditViewSet.as_view(), name='edit'),
]
