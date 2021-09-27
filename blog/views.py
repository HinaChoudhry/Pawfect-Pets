from django.shortcuts import render, redirect, reverse, get_object_or_404
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
            return redirect(reverse('blog'))
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


def edit_blog_post(request, blogpost_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('home'))

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect('blog')
            
        else:
            messages.error(
                    request,
                    'Failed to update the blog post.\
                    Please ensure the form is valid.')
    else:
        form = BlogPostForm(instance=blogpost)
        messages.info(request, f'You are editing {blogpost.blog_title}')

    template = 'blog/edit_blog.html'
    context = {
        'blogpost': blogpost,
        'form': form,
        
        
        
    }
    
    return render(request, template, context)