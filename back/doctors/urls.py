from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('appointments/',          AppointmentList.as_view(), name='appointment_list'),
    path('appointment/<int:aid>',  AppointmentRU.as_view(),   name='appointment_list'),
    path('appointment/make/<piin>/<diin>/<int:weekat>/<int:dateat>/<time>/', MakeAppointment.as_view(), name='make_appointment'),

    path('patient/requests/<iin>/', PatientRequestList.as_view(),    name='patient_request_list'),
    path('patient/history/<iin>/',  PatientHistoryList.as_view(),    name='patient_request_list'),

    path('doctor/schedule/<iin>/',  DoctorSchedule.as_view(),        name='doctor_schedule'),
    path('doctor/appointments/',    DoctorAppointmentList.as_view(), name='doctor_appointment_list'),
    path('doctor/patients/',        DoctorPatientList.as_view(),     name='doctor_patient_list'),

    path('doctors/',            DoctorList.as_view(), name='doctors'),
    path('doctor/<pk>/',        DoctorR.as_view(),    name='doctorR'),
    path('doctor/update/<pk>/', DoctorU.as_view(),    name='doctorU'),
    path('doctors/<specialization>/<int:limit>/<int:offset>/', DoctorIINList.as_view(), name='doctors_spec_limit'),

    path('services/',                  ServiceList.as_view(),        name='services'),
    path('service/<pk>/',               ServiceR.as_view(),        name='services'),
    path('service/update/<pk>/',        ServiceU.as_view(),        name='services'),
    path('service/schedule/<sid>/',    ServiceSchedule.as_view(),    name='service_schedule'),
    path('service/requests/',          ServiceRequestList.as_view(), name='service_request_list'),
    path('service/request/<int:srid>', ServiceRequestRU.as_view(),   name='service_list'),
    path('service/<department>/<int:limit>/<int:offset>/',                 ServiceDepartmentList.as_view(), name='services'),
    path('service/request/<piin>/<sid>/<int:weekat>/<int:dateat>/<time>/', RequestService.as_view(), name='request_service'),
]
