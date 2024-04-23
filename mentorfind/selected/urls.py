from django.urls import path
from .views import SelectedViewSet

urlpatterns = [
    path('', SelectedViewSet.as_view({'post': 'create', 'get': 'list'}))
]