from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Invalid username')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=19, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=123, null=True, blank=True)
    objects = AccountManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class AccountDetails(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=235, null=True, blank=True)
    passport_file = models.FileField(upload_to='passports/')

    def __str__(self):
        return self.user.phone


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = ("Telefon raqamni tasdiqlash")
        verbose_name_plural = ("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name="Telefon raqam")
    code = models.CharField(max_length=10, verbose_name="Kod")

    def __str__(self):
        return self.phone
