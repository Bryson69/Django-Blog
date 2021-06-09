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

