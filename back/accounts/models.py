from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, iin, password, is_superuser, is_staff, **extra_fields):
        if not iin:
            raise ValueError('The given IIN must be set')
        user = self.model(iin=iin, is_superuser=is_superuser, is_staff=is_staff, is_active=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, iin, password=None, **extra_fields):
        return self._create_user(iin, password, False, False, **extra_fields)

    def create_superuser(self, iin, password, **extra_fields):
        return self._create_user(iin, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # any fields you would like to add
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(null=True)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    iin         = models.CharField(max_length=12, primary_key=True)

    USERNAME_FIELD = 'iin'
    REQUIRED_FIELDS = []

    objects = UserManager()
