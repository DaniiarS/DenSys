from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from accounts.models import User

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_doctor(self, name, surname, middlename,
                        bddate, iin, id,
                        education, departament, specialization, category, photo, working_hours, duration, price,
                        contact_number, experience,
                        address, password, **extra_fields):
        values = [name, surname, middlename, bddate, id, education, departament, specialization, category, photo,
                  working_hours, duration, price, contact_number, experience, address, password]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        user = self.model(
            name=name, surname=surname, middlename=middlename,
            bddate=bddate, iin=iin, id=id,
            education=education, departament=departament, specialization=specialization, category=category, photo=photo,
            working_hours=working_hours, duration=duration, price=price,
            contact_number=contact_number, experience=experience,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_doctor(self, name, surname, middlename,
                        bddate, iin, id,
                        education, departament, category, photo,
                        working_hours, duration, price, specialization,
                        contact_number, experience,
                        address, password, **extra_fields):
        return self._create_doctor(self, name, surname, middlename,
                        bddate, iin, id,
                        education, departament, category, photo,
                        working_hours, duration, price, specialization,
                        contact_number, experience,
                        address, password, **extra_fields)

class Doctor(User):
    use_in_migrations = True
    name           = models.CharField(max_length=200)
    surname        = models.CharField(max_length=200)
    middlename     = models.CharField(max_length=200)
    bddate         = models.CharField(max_length=10)
    id             = models.CharField(max_length=12)
    education      = models.CharField(max_length=3)
    departament    = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    category       = models.CharField(max_length=200)
    photo          = models.FileField(upload_to='images/')
    working_hours  = models.JSONField(default=list)
    duration       = models.CharField(max_length=5)
    price          = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=12)
    experience     = models.CharField(max_length=3)
    url            = models.CharField(max_length=200, blank=True)
    address        = models.CharField(max_length=200)

    USERNAME_FIELD = "iin"
    REQUIRED_FIELD = ["name", "surname", "middlename", "bddate", "id", "education", "departament", "specialization", "category", "photo", "working_hours", "duration", "price", "contact_number", "experience", "address", "password"]
    objects=AccountManager()

