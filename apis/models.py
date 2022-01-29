from enum import unique
from hashlib import blake2b
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        """Create Save a User"""
        if not phone:
            raise ValueError('User must have a Email')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if user:
            return user

    def create_superuser(self, phone, password,**extra_fields):
        """Create and Save a super User"""
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_shopkeeper = False
        user.is_superuser = True
        user.save(using=self._db)

        return user
        


class User(AbstractBaseUser, PermissionsMixin):
    """"Custom Model"""
    phone = PhoneNumberField(unique=True,null=False,blank=False)
    is_shopkeeper = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return str(self.phone)