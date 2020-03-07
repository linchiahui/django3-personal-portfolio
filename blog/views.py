from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    Blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'all_blog.html', {'blogs' : Blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog})
