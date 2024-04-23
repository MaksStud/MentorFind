from django.urls import path
from .views import ViewHistoryViewSet

urlpatterns = [
    path('', ViewHistoryViewSet.as_view({'post': 'create', 'get': 'list'}, name='viewhistory')),
    path('<int:pk>/', ViewHistoryViewSet.as_view({'delete': 'destroy'})),
]