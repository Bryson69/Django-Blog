from django.contrib.auth import login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CreateComment

from .models import *
# Create your views here.

#
def home(request):
    context = { 'posts' : Post.objects.all()}
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app> / <model> <viewtype>.html
    context_object_name = 'posts' # naming the varible
    ordering = ['-date_posted']
    paginate_by = 8

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        if self.object.bookmark.filter(id=request.user.id).exists():
            self.object.bookmark.remove(request.user)
        else:
            self.object.bookmark.add(request.user)

        return redirect('blog-home', pk=self.object.pk)



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app> / <model> <viewtype>.html
    context_object_name = 'posts' # naming the varible
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

  
# def single_post(request, pk):

#     single_post = Post.objects.get(id = pk)

#     context = {'single_post': single_post}

#     return render(request, 'blog/single.html', context)



class PostDetailView(DetailView):
    model = Post
    extra_context ={'comment': Comment.objects.all()}
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','location','category','content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog-home')
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','location','category', 'tags', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('blog-home')
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
   
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('blog-home')
    

class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs
            ['category'])
        }
        return content

def category_list(request):

    category_list = Category.objects.exclude(name='default')
    context = {
        'category_list':category_list
        }
    return context

class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CreateComment
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('blog-home')


def search_post(request):
    if request.method == 'POST':
        search = request.POST['search']
        search_post = Post.objects.filter(title__contains=search)
        return render(request, 'blog/search.html',{'search':search, 'search_post':search_post})
    else:
        return render(request, 'blog/search.html', {'title': 'About'})



@login_required
def LikeView(request,pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
