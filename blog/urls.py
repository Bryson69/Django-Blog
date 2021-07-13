from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, LikeView, CreateComment

from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    
    path('post/<str:pk>/', PostDetailView.as_view(), name='post-detail'),

    # path('post/<str:pk>/', views.single_post, name='post-detail'),

    path('post-form/', PostCreateView.as_view(), name='post-create'), 

    path('article/<int:pk>/comment/', CreateComment.as_view(), name='add_comment'), 

    path('search-post/', views.search_post, name='search_post'), 
    
    path('post/<str:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('category/<category>/', views.CatListView.as_view(), name='category'),

    # on post id -->  path('post/<slug:slug:text>'),
    path('about/', views.about, name='about-page'),
  
]
