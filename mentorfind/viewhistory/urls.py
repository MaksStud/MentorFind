from django.urls import path
from .views import ViewHistoryViewSet

urlpatterns = [
    path('', ViewHistoryViewSet.as_view({'post': 'create', 'get': 'list'}, name='viewhistory')),
    path('<int:pk>/', ViewHistoryViewSet.as_view({'delete': 'destroy'})),
    path('get_for_author/', ViewHistoryViewSet.as_view({'get': 'get_for_author'}), name='get_for_author')
]