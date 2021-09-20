from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm


# Create your views here.
@login_required
def add_review(request, product_id):
    """ Add a review to the store """
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Successfully added review')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid')
    else:
        form = ReviewForm()
        
    template = 'products/products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, product_id):
    """ Edit a review in the store """

    review = get_object_or_404(Review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[review.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are reviewing {product.name}')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that')
        return redirect(reverse('home'))
        
    review = get_object_or_404(Review)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('products'))