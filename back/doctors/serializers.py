from rest_framework import serializers
from .models import Doctor
from django.contrib.auth.hashers import make_password

class DoctorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(DoctorSerializer, self).create(validated_data)

    class Meta:
        model = Doctor
        fields = ["name", "surname", "middlename", "bddate", "iin", "id", "education", "departament", "specialization", "category", "photo", "working_hours", "duration", "price", "contact_number", "experience", "address", "password"]
