from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from main.models import Request
from main.forms import RequestForm
from main.forms import RequestFormAdmin
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'email_verify', 'user_role', 'phone')
    UserAdmin.fieldsets += (('Extra Fields', {'fields': ('email_verify', 'user_role', 'phone', 'address')}),)


@admin.register(Request)
class RequestAdmin(ModelAdmin):
    form = RequestFormAdmin

    list_display = ('title', 'createdBy')
