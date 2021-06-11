from django.urls import path, include

from django.contrib.auth import views as auth_views

from . import views

from .forms import UserLoginForm

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=UserLoginForm), name='login'),

    path('register/', views.registerPage, name='register'),

    path('profile/', views.profilePage, name='profile'),
]
