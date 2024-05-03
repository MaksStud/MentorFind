from django.urls import path
from .authentication import RegisterView, LoginView
from .views import CustomUserReadViewSet, CustomUserEditViewSet, TopUsersViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get/<int:pk>/', CustomUserReadViewSet.as_view({'get': 'retrieve'}), name='get'),
    path('edit/<int:pk>/', CustomUserEditViewSet.as_view(), name='edit'),
    path('top/', TopUsersViewSet.as_view({'get': 'list'}), name='top')
]