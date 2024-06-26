from django.urls import path
from .authentication import RegisterView, LoginView
from .views import (CustomUserReadViewSet, CustomUserEditViewSet,
                    TopUsersViewSet, CustomUserReadViaTokenViewSet,
                    DeleteUserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get/<int:pk>/', CustomUserReadViewSet.as_view({'get': 'retrieve'}), name='get'),
    path('getViaToken/', CustomUserReadViaTokenViewSet.as_view({'get': 'get'})),
    path('edit/', CustomUserEditViewSet.as_view(), name='edit'),
    path('top/', TopUsersViewSet.as_view({'get': 'list'}), name='top'),
    path('delete/', DeleteUserViewSet.as_view({'delete': 'destroy'}, name='delete'))
]