from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class DoctorIINSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["iin"]

class DoctorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(DoctorSerializer, self).create(validated_data)

    class Meta:
        model = Doctor
        fields = ["name", "surname", "middlename", "bddate", "iin", "id", "education", "department", "specialization", "category", "photo", "working_hours", "duration", "price", "contact_number", "experience", "address", "password"]
        extra_kwargs = {'password': {'write_only': True}}

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    class Meta:
        model = Appointment
        fields = ["status", "patient", "doctor", "date", "time"]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "department", "price", "working_hours", "duration"]

class ServiceRequestSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    class Meta:
        model = ServiceRequest
        fields = '__all__'

