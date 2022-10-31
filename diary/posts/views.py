from django.shortcuts import render, HttpResponse
from .models import Post, User

def index(request):
    '''Выводит последние добавленные посты.'''
    template = 'posts/index.html'

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, template, context)

def group_list(request, slug):
    text = f'Группа номер {slug}'
    template = 'posts/group_list.html'

    context = {
        'text': text
    }

    return render(request, template, context)
