from django.contrib import admin
from django.urls import path, include
from .views import DoctorViewSet, DoctorsView, DoctorView

urlpatterns = [
    path('doctors/', DoctorViewSet.as_view(), name='doctors'),
    path('doctor/<iin>/', DoctorViewSet.as_view(), name='doctor'),
]
