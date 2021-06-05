from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/', views.single_post, name='single-blog'),
    path('about/', views.about, name='about-page'),

    # registration    
]
