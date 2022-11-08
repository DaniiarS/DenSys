from django.contrib import admin
from django.urls import path, include
from .views import PatientsView,PatientView

urlpatterns = [
    path('patients/', PatientsView, name='patients'),
    path('patient/<iin>/', PatientView, name='patient'),
]
