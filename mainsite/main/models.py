from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _('Email'),
        max_length=254,
        unique=True
    )

    email_verify = models.BooleanField(default=False)
    user_role = models.CharField(default='клиент', max_length=55)
