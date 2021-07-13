from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from .models import Profile
# https://docs.djangoproject.com/en/3.0/topics/auth/default/
# https://docs.djangoproject.com/en/3.0/topics/forms/

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
    {
        'class': 'form-control mb-3', 
        'placeholder': 'Username', 
        'id': 'login-username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'login-pwd',
    }))

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'bio', 'banner', 'profile_pic']
