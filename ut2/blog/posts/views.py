from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddPostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post/list.html', {'posts': posts})


def post_detail(request, post_slug: str):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'posts/post/detail.html', {'post': post})


def add_post(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():
            post_title = form.cleaned_data['title']

            post_content = form.cleaned_data['content']

            post_slug = slugify(post_title)

            Post.objects.create(
                title=post_title,
                content=post_content,
                slug=post_slug,
            )
            return redirect('posts:post-list')

    else:
        form = AddPostForm()

    return render(request, 'posts/post/add.html', {'form': form})
