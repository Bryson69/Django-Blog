from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    
    path('post/<str:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post-form/', PostCreateView.as_view(), name='post-create'), 

    path('post/<str:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('category/<category>/', views.CatListView.as_view(), name='category'),

    # on post id -->  path('post/<slug:slug:text>'),
    path('about/', views.about, name='about-page'),

    path('project-overview/', views.projectOverview, name='project-overview'),


    # registration    
]
