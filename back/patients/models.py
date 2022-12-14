from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from accounts.models import User

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_patient(self, name, surname, middlename,
                        bddate, iin, id,
                        blood_type, marital_status,
                        contact_number, emergency_contact_number,
                        address, password, **extra_fields):
        values = [name, surname, middlename, bddate, iin, id, blood_type, marital_status, contact_number, emergency_contact_number, address, password]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        user = self.model(
            name=name, surname=surname, middlename=middlename,
            bddate=bddate, iin=iin, id=id,
            blood_type=blood_type, marital_status=marital_status,
            contact_number=contact_number, emergency_contact_number=emergency_contact_number,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_patient(self, name, surname, middlename,
                        bddate, iin, id,
                        blood_type, marital_status,
                        contact_number, emergency_contact_number,
                        address, password, **extra_fields):
        #extra_fields.setdefault('is_staff', False)
        #extra_fields.setdefault('is_superuser', False)
        return self._create_patient(self, name, surname, middlename,
                                    bddate, iin, id,
                                    blood_type, marital_status,
                                    contact_number, emergency_contact_number,
                                    address, password, **extra_fields)

class Patient(User):
    use_in_migrations = True
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    bddate = models.CharField(max_length=10)
    #iin = models.CharField(max_length=12, primary_key=True)
    id = models.CharField(max_length=12)
    blood_type = models.CharField(max_length=3)
    marital_status = models.CharField(max_length=8)
    contact_number = models.CharField(max_length=12)
    emergency_contact_number = models.CharField(max_length=12)
    email = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)

    USERNAME_FIELD = "iin"
    REQUIRED_FIELD = ["name", "surname", "middlename", "bddate", "id", "blood_type", "marital_status", "contact_number", "emergency_contact_number", "address", "password"]
    objects=AccountManager()

