from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


def blog_detail(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    form = BlogCommentForm()
    comments = BlogComment.objects.filter(blogpost=blogpost)

    context = {
        'blogpost': blogpost,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
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


@login_required
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


@login_required
def delete_blog_post(request, blogpost_id):
    """ Delete a review from the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that')
        return redirect(reverse('home'))
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    blogpost.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('blog'))


@login_required
def add_blog_comment(request, blogpost_id):
    """ Add a blog comment """
    
    if request.method == 'POST':
        form = BlogCommentForm(request.POST, request.FILES)
        if form.is_valid():
            blogcomment = form.save(commit=False)
            messages.success(request, 'Successfully added comment')
            return redirect(reverse('blog_detail', args=[blogpost_id]))
        else:
            messages.error(request, 'Failed to add blog comment. Please ensure the form is valid.')
    else:
        form = BlogCommentForm()
        
    template = 'blog_detail.html'
    context = {
       
        'blogcomment': blogcomment,
        'form': form,
        
       
    }

    return render(request, template, context)