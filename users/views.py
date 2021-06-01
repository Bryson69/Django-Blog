from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm

from .forms import UserRegistrationForm

from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form  = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect ('login')

    form  = UserRegistrationForm()
    return render(request, 'auth/register.html',  {'form': form} )

def login(request):
    return render(request, 'auth/login.html')