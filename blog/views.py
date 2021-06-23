from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required


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


# def single_post(request, pk):

#     single_post = Post.objects.get(id = pk)

#     context = {'single_post': single_post}

#     return render(request, 'blog/single.html', context)



class PostDetailView(DetailView):
    model = Post
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','location','category','content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
    
