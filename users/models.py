from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(_("Email address"), unique=True)
    full_name = models.CharField(_('Fullname'), max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email
