from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    text = "Это главная страница проекта Yatube"
    context = {"text": text}
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    text = "Здесь будет информация о группах проекта Yatube"
    context = {"text": text}
    template = 'posts/group_list.html'
    return render(request, template, context)
