from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Category, Comment

def main(request):
    return render(request, 'blog/main.html')

def users(request):
    users_list = User.objects.all()
    return render(request, 'blog/users.html', {'users': users_list})

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts})

def categories(request):
    categories_list = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories_list})

def comments(request):
    comments_list = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments_list})

def blogdetails(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blogdetails.html', {'post': post})