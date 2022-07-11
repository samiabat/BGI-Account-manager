
from django.urls import path
from . import views

urlpatterns = [
    path('sectors/', views.sectorAPI),
    path('sectors/<str:pk>/', views.sectorAPI),
    path('employees/', views.employeeAPI),
    path('employees/<str:pk>/', views.employeeAPI),
    path('roles/', views.roleAPI),
    path('roles/<str:pk>/', views.roleAPI),
    path('employeeSectors/', views.employeeSectorAPI),
    path('employeeSectors/<str:pk>/', views.employeeSectorAPI),
]
