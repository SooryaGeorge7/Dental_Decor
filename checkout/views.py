from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('shoppingbag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('shop_products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O5RLNLXDIjnmjWheHiUGv8gpdHMztxkDgtdzfObaHWCHdsPUAUFQvrpzc3DzY1pI9I31BNXo0cO5lq2ihwvfEDg00U4BEMhwh',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)