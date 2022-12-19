from cProfile import label

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from main.utils import send_email

from main.models import Request

from main.models import Feedback

User = get_user_model()


class AuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
            if not self.user_cache.email_verify:
                send_email(self.request, self.user_cache)
                raise ValidationError(
                    'Почта не верифицирована! Проверьте свою почту',
                    code="invalid_login",
                )

        return self.cleaned_data


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class UserChangeForm(UserChangeForm):
    first_name = forms.CharField(
        label=_("Имя"),
        max_length=25,
        widget=forms.TextInput(attrs={"autocomplete": "given-name", 'placeholder': 'Имя'})
    )

    last_name = forms.CharField(
        label=_("Фамилия"),
        max_length=35,
        widget=forms.TextInput(attrs={"autocomplete": "family-name", 'placeholder': 'Фамилия'})
    )

    phone = forms.CharField(
        label=_("Номер телефона"),
        max_length=12,
        widget=forms.TextInput(attrs={"autocomplete": "postal-code", 'placeholder': 'Номер телефона'}),
        required=False
    )

    addr = forms.CharField(
        label=_("Адрес"),
        max_length=254,
        widget=forms.Textarea(attrs={"autocomplete": "street-address", 'placeholder': 'Адрес'}),
        required=False
    )

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'address')


class RequestForm(forms.ModelForm):
    title = forms.CharField(
        label=_("Название"),
        widget=forms.TextInput()
    )

    content = forms.CharField(
        label=_("Контент"),
        widget=forms.Textarea()
    )
    file = forms.FileField(
        label=_("Прикрепить ТЗ"),
        widget=forms.ClearableFileInput()
    )

    class Meta:
        model = Request
        fields = ('createdBy', 'title', 'content', 'leads', 'file')
        widgets = {'createdBy': forms.HiddenInput(), 'leads': forms.HiddenInput()}


class RequestFormAdmin(RequestForm):
    def __init__(self, *args, **kwargs):
        super(RequestFormAdmin, self).__init__(*args, **kwargs)
        self.fields['leads'].queryset = User.objects.filter(user_role='eng')
        self.fields['createdBy'].queryset = User.objects.filter(user_role='client')

    class Meta:
        model = Request
        fields = ('createdBy', 'title', 'content', 'status', 'leads', 'file', 'date')


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Имя"),
        max_length=25,
        widget=forms.TextInput(attrs={"autocomplete": "given-name", 'placeholder': 'Имя'})
    )

    phone = forms.CharField(
        label=_("Номер телефона"),
        max_length=12,
        widget=forms.TextInput(attrs={"autocomplete": "postal-code", 'placeholder': 'Номер телефона'}),
        required=False
    )

    email = forms.EmailField(
        label=_("Почта"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    content = forms.CharField(
        label=_("Содержание"),
        widget=forms.Textarea()
    )

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'email', 'content')
