from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'Admin'
    USER = 'User'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)  
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=USER)
    alert_value = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  

    objects = CustomUserManager()

    USERNAME_FIELD = "email"  
    REQUIRED_FIELDS = ["username"]  

    def save(self,*args,**kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.username
