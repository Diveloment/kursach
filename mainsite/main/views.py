from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.views import View
from main.forms import UserCreationForm

from main.models import User

from main.utils import send_email

from main.forms import AuthenticationForm

User = get_user_model()

def index(request):
    data = {
        'title': 'Homepage',
        'values': [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
    return render(request, 'main/index.html', data)


def logout_view(request):
    return render(request, 'registration/logout.html')


class MyLoginView(LoginView):
    form_class = AuthenticationForm


class EmailVerify(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password1)
            send_email(request, user)
            return redirect('confirm_email')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class AccountView(View):
    template_name = 'main/account.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)