
from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sectors/', views.sectorAPI),
    path('sectors/<str:pk>/', views.sectorAPI),
    path('employees/', views.employeeAPI),
    path('employees/<str:pk>/', views.employeeAPI),
    path('roles/', views.roleAPI),
    path('roles/<str:pk>/', views.roleAPI),
    path('employeeSectors/', views.employeeSectorAPI),
    path('employeeSectors/<str:pk>/', views.employeeSectorAPI),
    path('stastics/', views.stasticsAPI),
    
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
