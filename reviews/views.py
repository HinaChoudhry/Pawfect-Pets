from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from products.models import Product


# Create your views here.
@login_required
def add_review(request, product_id):
    """ Add a review to a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user.userprofile
            review.save()
            messages.success(request, 'Successfully added review')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(
                request,
                'Failed to add review. Please ensure the form is valid')
    else:
        form = ReviewForm()

    template = 'products/products.html'
    context = {
        'form': form,

    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id, product_id):
    """ Edit a review in the store """

    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':

        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(
            request, f'You are editing your review for {product.name}')

    context = {
        'form': form,
        'review': review,
        'product_id': product_id,
        'review_id': review_id,
    }

    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, review_id,  product_id):
    """ Delete a review from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('products'))
