from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["name", "surname", "middlename", "date", "iin", "id", "blood_type", "marital_status", "contact_number", "emergency_contact_number", "email", "address", "password"]

