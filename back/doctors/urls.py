from django.contrib import admin
from django.urls import path, include
from .views import DoctorList, DoctorRUD

urlpatterns = [
    path('doctors/',     DoctorList.as_view(), name='doctors'),
    path('doctor/<pk>/', DoctorRUD.as_view(), name='doctor'),
]
