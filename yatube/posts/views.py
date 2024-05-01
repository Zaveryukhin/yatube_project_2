from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = 'posts/index.html'
    return render(request, template)

    # return HttpResponse(
    #     'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
    #     'если у тебя нет правильных <s>вопросов</s> запросов.'
    # )


def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)
