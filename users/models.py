from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    first_name = models.CharField(max_length=150, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='Последний вход')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    birthdate = models.DateField(blank=True, null=True)
    

    google_id = models.CharField(max_length=255, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    
# class User(AbstractUser):
#     first_name = models.CharField(max_length=150, verbose_name='Имя')
#     last_name = models.CharField(max_length=150, verbose_name='Фамилия', blank=True, null=True)
#     last_login = models.DateTimeField(blank=True, null=True, verbose_name='Последний вход')

#     google_id = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'