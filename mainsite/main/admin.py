from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from main.models import Request

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'email_verify', 'user_role', 'phone')
    UserAdmin.fieldsets += (('Extra Fields', {'fields': ('email_verify', 'user_role', 'phone', 'address')}),)


@admin.register(Request)
class RequestAdmin(ModelAdmin):
    list_display = ('title', 'createdBy')
