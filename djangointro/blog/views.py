from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def show_blogs(request):
    all_blogs = Blog.objects.all()
    context = {
        "blogs": all_blogs,
    }
    return render(request, 'blog/index.html', context)


def create_blog(request):
    if request.method == "GET":
        form = BlogForm()
        context = {
            "form": form,
        }
        return render(request, 'blog/create_blog.html', context)
    elif request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all')
            