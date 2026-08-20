from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    breadcrumbs = [
        {'name': 'Блог', 'url': ''},
    ]
    return render(request, 'blog/blog_list.html', {'posts': posts, 'breadcrumbs': breadcrumbs})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    breadcrumbs = [
        {'name': 'Блог', 'url': '/blog/'},
        {'name': post.title, 'url': ''},
    ]
    return render(request, 'blog/blog_detail.html', {'post': post, 'breadcrumbs': breadcrumbs})