from django.contrib import admin
from django.urls import path
from app1.views import (
    LandingPageView,
    AddDonationView,
    LoginView,
    RegisterView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='main'),
    path('form/', AddDonationView.as_view(), name='form'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]