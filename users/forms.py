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


# class RegistrationForm(forms.ModelForm):

#     username = forms.CharField(
#         label='Enter Username', min_length=4, max_length=50, help_text='Required')
#     email = forms.EmailField(max_length=100, help_text='Required', error_messages={
#         'required': 'Sorry, you will need an email'})
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label='Repeat password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name',)

#     def clean_username(self):
#         username = self.cleaned_data['username'].lower()
#         r = User.objects.filter(username=username)
#         if r.count():
#             raise ValidationError("Username already exists")
#         return username

#     def clean_password2(self):
#         pass_check = self.cleaned_data
#         if pass_check['password'] != pass_check['password2']:
#             raise forms.ValidationError('Passwords do not match.')
#         return pass_check['password2']

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError(
#                 'Please use another Email, that is already taken')
#         return email

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update(
#             {'class': 'form-control mb-3', 'placeholder': 'Username'})
#         self.fields['email'].widget.attrs.update(
#             {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
#         self.fields['password'].widget.attrs.update(
#             {'class': 'form-control', 'placeholder': 'Password'})
#         self.fields['password2'].widget.attrs.update(
#             {'class': 'form-control', 'placeholder': 'Repeat Password'})



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
