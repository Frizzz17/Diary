from re import template
from django.shortcuts import get_object_or_404, render

from .models import Post, User, Group


def index(request):
    '''Выводит последние добавленные посты.'''
    template = 'posts/index.html'
    count = 2

    posts = Post.objects.all()

    context = {
        'posts': posts,
        'count': count
    }

    return render(request, template, context)


def group_list(request, slug):
    '''Выводит посты принадлежащие только данной группе.'''
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()

    context = {
       'posts': posts 
    }

    return render(request, template, context)


def profile(request, username):
    '''Выводит посты пользователя.'''
    template = 'posts/profile.html'

    user = get_object_or_404(User, username=username)
    posts = user.posts.all()

    context = {
        'posts': posts
    }

    return render(request, template, context)


def post_detail(request, post_id):
    '''Выводит детали поста.'''
    post = Post.objects.get(id=post_id)