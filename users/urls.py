from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

from .forms import UserLoginForm

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=UserLoginForm), name='login'),

    path('logout/', views.logout, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('profile/', views.profilePage, name='profile'),
    path('update-profile/', views.updateProfile, name='update-profile'),

    path('like/', views.like, name='like'),
    
    path('bookmark/<str:id>/', views.bookmark_add, name='bookmark_add'),
    path('bookmarks/', views.bookmark_list, name='bookmark_list'),
]
