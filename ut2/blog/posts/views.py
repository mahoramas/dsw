from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post/list.html', {'posts': posts})


def post_detail(request, post_slug: str):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'posts/post/detail.html', {'post': post})
