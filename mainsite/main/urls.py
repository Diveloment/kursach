from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

from . import views
from .views import Register, EmailVerify, MyLoginView, AccountView, AccountViewRequests

urlpatterns = [
    path('', views.index, name='home'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('auth/login/', MyLoginView.as_view(), name='login'),
    path('auth/', include('django.contrib.auth.urls')),
    path('account/profile', AccountView.as_view(), name='profile'),
    path('account/requests', AccountViewRequests.as_view(), name='requests'),
    path('register/', Register.as_view(), name='register'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
]
