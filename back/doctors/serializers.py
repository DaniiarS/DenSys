from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["name", "surname", "middlename", "date", "iin", "id", "education", "departament", "specialization", "category", "contact_number", "experience", "address", "password"]

