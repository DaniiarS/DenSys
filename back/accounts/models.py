from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, iin, password, is_superuser, **extra_fields):
        now = timezone.now()
        if not iin:
            raise ValueError('The given IIN must be set')
        user = self.model(iin=iin, is_active=True, is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # any fields you would like to add
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)
    iin = models.CharField(max_length=12, primary_key=True)

    USERNAME_FIELD = 'iin'
    REQUIRED_FIELDS = []

    objects = UserManager()
