from django.urls import path
from .views import TextGenerationViewSet, ImageGenerationViewSet

urlpatterns = [
    path('getText/', TextGenerationViewSet.as_view({'get': 'retrieve'}), name='getTest'),
    path('getPhoto/', ImageGenerationViewSet.as_view({'get': 'retrieve'}), name='getPhoto'),

]