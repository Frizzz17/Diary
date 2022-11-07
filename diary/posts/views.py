from django.shortcuts import get_object_or_404, render

from .models import Post, User, Group
from .utils import paginator


def index(request):
    '''Выводит последние добавленные посты.'''
    template = 'posts/index.html'
    posts = Post.objects.all()
    page_obj = paginator(request, posts)

    context = {
        'page_obj': page_obj
    }

    return render(request, template, context)


def group_list(request, slug):
    '''Выводит посты принадлежащие только данной группе.'''
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    page_obj = paginator(request, posts)

    context = {
       'page_obj': page_obj 
    }

    return render(request, template, context)


def profile(request, username):
    '''Выводит посты пользователя.'''
    template = 'posts/profile.html'

    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    page_obj = paginator(request, posts)

    context = {
        'page_obj': page_obj,
        'author': author
    }

    return render(request, template, context)


def post_detail(request, post_id):
    '''Выводит детали поста.'''
    template = 'posts/post_detail.html'
    post = Post.objects.get(id=post_id)
    user = post.author
    posts_num = user.posts.count()

    Post.objects.filter(id=post_id).update(count=post.count + 1)

    context = {
        'post': post,
        'posts_num': posts_num
    }

    return render(request, template, context)
