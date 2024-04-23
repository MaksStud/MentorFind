from django.urls import path
from .views import ViewHistoryViewSet

urlpatterns = [
    path('viewhistory/', ViewHistoryViewSet.as_view({'post': 'create', 'get': 'list'}, name='viewhistory')),
]