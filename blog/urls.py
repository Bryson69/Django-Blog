from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    
    path('post/<str:pk>/', views.single_post, name='post'),

    path('category/<category>/', views.CatListView.as_view(), name='category'),
    # on post id -->  path('post/<slug:slug:text>'),
    path('about/', views.about, name='about-page'),

    # registration    
]
