from django.urls import path
from .views import ViewHistoryViewSet, ViewHistoryViewGet

urlpatterns = [
    path('', ViewHistoryViewSet.as_view({'post': 'create',}, name='viewhistory')),
    path('getlist/', ViewHistoryViewGet.as_view({'get': 'list'}, name='viewhistory')),
    path('<int:pk>/', ViewHistoryViewSet.as_view({'delete': 'destroy'})),
    path('del-full-viewhistory/', ViewHistoryViewSet.as_view({'delete': 'delete_full_viewhistory'})) #Apply for DELETE
]