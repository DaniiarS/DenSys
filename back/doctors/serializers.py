from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["name", "surname", "middlename", "date", "iin", "id", "education", "departament", "specialization", "category", "photo", "contact_number", "experience", "address", "password"]


class FileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    photo    = serializers.FileField(max_length=100)

    def create(self, validated_data):
        import json
        print("Hello")
        profile_data = validated_data.pop('name')
        print(type(profile_data))
        doctor = Doctor.objects.create(name=profile_data)
        return doctor

