from django.urls import path
from .views import SelectedViewSet

urlpatterns = [
    path('', SelectedViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('del/<int:pk>/', SelectedViewSet.as_view({'delete': 'destroy'})),
]