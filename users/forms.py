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

    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})







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
