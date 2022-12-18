from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


from . import views
from .views import Register, EmailVerify, MyLoginView, AccountView, AccountViewRequests, AccountViewMyRequests, ReqView

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', TemplateView.as_view(template_name='main/services.html'), name='services'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('auth/login/', MyLoginView.as_view(), name='login'),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', TemplateView.as_view(template_name='main/about.html'), name='about'),
    path('account/profile', AccountView.as_view(), name='profile'),
    path('account/requests', AccountViewRequests.as_view(), name='requests'),
    path('account/my_requests', AccountViewMyRequests.as_view(), name='my_requests'),
    path('account/my_requests/<int:pk>', ReqView.as_view(), name='req_detail'),
    path('register/', Register.as_view(), name='register'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
