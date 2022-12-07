from rest_framework import serializers
from .models import *
from patients.serializers import *
from patients.models      import *
from django.contrib.auth.hashers import make_password

class DoctorIINSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["iin"]

class DoctorPatientModel(models.Model):
    use_in_migrations = False
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pcount      = models.IntegerField()

class DoctorPatientSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    class Meta:
        model  = DoctorPatientModel
        fields = ['patient', 'pcount']

class DoctorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(DoctorSerializer, self).create(validated_data)

    class Meta:
        model = Doctor
        fields = ["name", "surname", "middlename", "bddate", "iin", "id", "education", "department", "specialization", "category", "photo", "working_hours", "duration", "price", "contact_number", "experience", "address", "password"]
        extra_kwargs = {'password': {'write_only': True}}

class AppointmentSerializer(serializers.ModelSerializer):
    doctor  = DoctorSerializer()
    patient = PatientSerializer()
    class Meta:
        model = Appointment
        fields = ["id", "status", "patient", "doctor", "date", "time"]

class AppointmentStatusSerializer(serializers.ModelSerializer):
    aid = AppointmentSerializer()
    class Meta:
        model = AppointmentStatus
        fields = '__all__'

class AppointmentUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["status"]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "department", "price", "working_hours", "duration"]

class ServiceRequestSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    patient = PatientSerializer()
    class Meta:
        model = ServiceRequest
        fields = '__all__'


class ServiceRequestStatusSerializer(serializers.ModelSerializer):
    srid = ServiceRequestSerializer()
    class Meta:
        model = ServiceRequestStatus
        fields = '__all__'

class ServiceRequestUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ["status"]

