from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import BlogPostForm, BlogCommentForm
from .models import BlogPost, BlogComment


def blog(request):
    """ This view returns the blog page"""
    blogposts = BlogPost.objects.all().order_by("-date")
    form = BlogPostForm()
    
    template = 'blog/blog.html'
    context = {
      'blogposts': blogposts,
      'form': form,
    }

    return render(request, template, context)



def add_blog_post(request):
    """ Add a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost = form.save()
            messages.success(request, 'Successfully added blog post')
            return redirect(reverse('blog', args=[product.id]))
        else:
            messages.error(request, 'Failed to add blog post. Please ensure the form is valid.')
    else:
        form = BlogPostForm()
        
    template = 'blog/blog.html'
    context = {
        'blogposts': blogposts,
        'form': form,
       
    }

    return render(request, template, context)