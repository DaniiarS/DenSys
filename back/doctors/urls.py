from django.contrib import admin
from django.urls import path, include
from .views import DoctorsView, DoctorView

urlpatterns = [
    path('doctors/', DoctorsView, name='doctors'),
    path('doctor/<iin>/', DoctorView, name='doctor'),
]
