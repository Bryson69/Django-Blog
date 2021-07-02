from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .token import account_activation_token
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm, AuthenticationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from blog.models import Post

def registerPage(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# def loginPage(request):
#     return render(request, 'registration/login.html')


@login_required
def profilePage(request):
    context = {}
    return render(request, 'registration/profile.html', context)

@login_required
def updateProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated!')
            return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
        
    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'registration/update_profile.html', context)


@login_required
def logout(request):
    django_logout(request)
    return redirect('login')


@ login_required
def bookmark_add(request, id):
    post = get_object_or_404(Post, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@ login_required
def bookmark_list(request):
    new = Post.bookmarkmanager.filter(favourites=request.user)
    return render(request, 'registration/bookmark.html',{'new': new})

