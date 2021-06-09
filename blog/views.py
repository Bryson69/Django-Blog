from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView

from .models import *
# Create your views here.

#
def home(request):

    context = { 'posts' : Post.objects.all()}

    return render(request, 'blog/home.html', context)


def single_post(request, pk):

    single_post = Post.objects.get(id = pk)

    context = {'single_post': single_post}

    return render(request, 'blog/single.html', context)


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

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})