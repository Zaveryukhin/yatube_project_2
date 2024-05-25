from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    text = "Здесь будет информация о группах проекта Yatube"
    context = {"text": text}
    template = 'posts/group_list.html'
    return render(request, template, context)
