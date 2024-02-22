# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet

router = DefaultRouter()
router.register(r'new_advert', AdvertisementViewSet)

urlpatterns = [
    path('new_advert/', include(router.urls)),
]
