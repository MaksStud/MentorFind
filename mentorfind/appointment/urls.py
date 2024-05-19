from django.urls import path
from .views import AppointmentViewSet, AppointmentListViewSet

urlpatterns = [
    path('', AppointmentViewSet.as_view({'post': 'create'})),
    path('del/<int:pk>/', AppointmentViewSet.as_view({'delete': 'destroy'})),
    path('getList/', AppointmentListViewSet.as_view({'get': 'list'}))
]
