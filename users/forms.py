from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# https://docs.djangoproject.com/en/3.0/topics/auth/default/
# https://docs.djangoproject.com/en/3.0/topics/forms/



class UserRegistrationForm(UserCreationForm):

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