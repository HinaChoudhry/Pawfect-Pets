from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JRYfiDHrdWivGAqkjRAnefLgSuhmgihDf0DvXE1ZceMoM2gyCSnyf59cLEpoJNRfbcTrsqq4T9w43aLoFMwSC4J000WRnWTTR'
    }

    return render(request, template, context)