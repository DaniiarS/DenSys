from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('appointment/<piin>/<diin>/<int:weekat>/<int:dateat>/<time>/', MakeAppointment.as_view(), name='make_appointment'),
    path('appointments/', AppointmentList.as_view(), name='appointment_list'),
    path('doctors/',     DoctorList.as_view(), name='doctors'),
    path('doctor/schedule/<iin>/', DoctorSchedule.as_view(), name='doctor_schedule'),
    path('doctor/update/<pk>/', DoctorU.as_view(),    name='doctorU'),
    path('doctor/<pk>/', DoctorR.as_view(),    name='doctorR'),
    path('doctors/<specialization>/<int:limit>/<int:offset>/', DoctorIINList.as_view(), name='doctors_spec_limit'),
    path('doctors/<specialization>', DoctorIINList.as_view(), name='doctors_spec'),
]
