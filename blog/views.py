from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import BlogPostForm, BlogCommentForm
from .models import BlogPost, BlogComment

def blog(request):
    """ This view returns the blog page"""
    blogposts = BlogPost.objects.all().order_by("-date")

    
    template = 'blog/blog.html'
    context = {
      'blogposts': blogposts
    }

    return render(request, template, context)



## Add def add_blog_post here to link up the add post button on blog.html