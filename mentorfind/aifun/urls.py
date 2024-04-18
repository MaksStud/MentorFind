from django.urls import path
from .views import TaskResponseViewSet

urlpatterns = [
    path('get/', TaskResponseViewSet.as_view({'get': 'retrieve'}), name='get'),
]