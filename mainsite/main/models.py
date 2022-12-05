from enum import unique

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USER_ROLES = (
        ('admin', 'админ'),
        ('client', 'клиент'),
        ('eng', 'инжинер')
    )

    email = models.EmailField(
        _('Email'),
        max_length=254,
        unique=False,
        blank=True,
        null=True
    )

    email_verify = models.BooleanField(default=False)
    user_role = models.CharField(choices=USER_ROLES, default='client', max_length=55)
    phone = models.CharField(default='', max_length=12, unique=False, blank=True, null=True)
    address = models.CharField(default='', max_length=254, unique=False, blank=True, null=True)


class Request(models.Model):
    REQ_STATUS = (
        ('refused', 'отклонено'),
        ('accepted', 'принято'),
        ('awaiting', 'ожидание')
    )

    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdBy', verbose_name='заявитель')
    title = models.CharField(max_length=25, verbose_name='название')
    content = models.TextField(blank=True, verbose_name='содержание')
    status = models.CharField(max_length=15, choices=REQ_STATUS, default='awaiting', verbose_name='статус')
    leads = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='leads', null=True, blank=True, verbose_name='куратор')

    class Meta:
        verbose_name = _("заявка")
        verbose_name_plural = _("заявки")

