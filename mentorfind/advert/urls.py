from django.urls import path
from .views import (AdvertisementViewSet, ReviewViewSet,
                    AdvertisementGetByIdViewSet, AdvertisementEditViewSet,
                    ReviewByAdvertisementAPIView, GiveAllUserAdsAway)

urlpatterns = [
    path('adding-and-searching/', AdvertisementViewSet.as_view({'post': 'create', 'get': 'list'}), name='adding-and-searching'),
    path('review/', ReviewViewSet.as_view({'post': 'create', 'get': 'list'}), name='review'),
    path('get/<int:pk>/', AdvertisementGetByIdViewSet.as_view({'get': 'retrieve'}), name='getById'),
    path('edit/<int:pk>/', AdvertisementEditViewSet.as_view(), name='edit'),
    path('review-by-advertisement/<int:advertisement_id>/', ReviewByAdvertisementAPIView.as_view(), name='review-by-advertisement'),
    path('get-for-author/', GiveAllUserAdsAway.as_view({'get': 'list'}), name='get'),
    path('delete/<int:pk>/', AdvertisementViewSet.as_view({'delete': 'destroy'}), name='delete'),
]

