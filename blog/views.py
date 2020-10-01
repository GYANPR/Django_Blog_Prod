from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)


# we could call this view either with post id or slug
def detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)