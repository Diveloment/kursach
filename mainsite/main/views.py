from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.files.base import ContentFile, File
from django.views import View
from django.views.generic import DetailView
from main.forms import UserCreationForm
from main import models

from main.models import User

from main.models import Request

from main.utils import send_email

from main.forms import AuthenticationForm

from main.forms import UserChangeForm

from main.forms import RequestForm

User = get_user_model()


def get_user(uidb64):
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
        user = get_user(uidb64)

        if user and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')


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
    template_name = 'main/profile.html'

    def get(self, request):
        form = UserChangeForm()
        user = request.user

        form = UserChangeForm(initial={'first_name': user.first_name,
                                       'last_name': user.last_name,
                                       'phone': user.phone,
                                       'addr': user.address})

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserChangeForm(request.POST)
        user = request.user

        context = {
            'form': form,
            'answ': "Данные не записаны!",
            'error': True
        }

        if form.is_valid:
            login_data = request.POST.dict()
            frst_name = login_data.get("first_name")
            lst_name = login_data.get("last_name")

            user.first_name = frst_name
            user.last_name = lst_name
            user.phone = login_data.get("phone")
            user.address = login_data.get("addr")
            user.save()
            context = {
                'form': form,
                'answ': "Данные успешно записаны!"
            }
            return render(request, self.template_name, context)

        return render(request, self.template_name, context)


class AccountViewRequests(View):
    template_name = 'main/requests.html'

    def get(self, request):
        user = request.user
        form = RequestForm(initial={'createdBy': user})
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        form = RequestForm(request.POST, request.FILES)

        context = {
            'form': form,
            'answ': "Данные не записаны!"
        }

        if form.is_valid:
            form.save()
            context = {
                'form': RequestForm(initial={'createdBy': user}),
                'answ': "Данные успешно записаны!"
            }
            return render(request, self.template_name, context)

        return render(request, self.template_name, context)


class AccountViewMyRequests(View):
    template_name = 'main/my_req.html'

    def get(self, request):
        user = request.user
        is_staff = user.is_staff
        if is_staff:
            reqs = Request.objects.filter(leads=user)
            reqs = reqs.filter(status='accepted')
        else:
            reqs = Request.objects.filter(createdBy=user)
        reqs = reqs.order_by('status')
        context = {
            'reqs': reqs
        }
        return render(request, self.template_name, context)


class ReqView(DetailView):
    model = Request
    template_name = 'main/detail_view.html'
    context_object_name = 'req'
