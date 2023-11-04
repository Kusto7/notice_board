from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = PhoneNumberField(max_length=30, verbose_name='телефон', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Email')
    image = models.ImageField(upload_to="users/avatars", verbose_name="аватарка", **NULLABLE)
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.USER)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
