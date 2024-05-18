from django.urls import path
from .views import MessageListViewSet, MessageViewSet

urlpatterns = [
    path('new/', MessageViewSet.as_view({'post': 'create'})),
    path('get/', MessageListViewSet.as_view({'get': 'list'})),
    path('del/<int:pk>/', MessageViewSet.as_view({'delete': 'destroy'}))
]