from django.urls import path, re_path
from .authentication import RegisterView, LoginView
from .views import CustomUserViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get/<int:pk>/', CustomUserViewSet.as_view({'get': 'retrieve'}), name='get'),
]