from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51S8Ik3CNa0cNqqRjaxpVCrfzAZXZEu2vP6ixDmfRAMYJQYN1npWaxdYeIDa2yF1qt0Sc3Mg72t8WjpwWsqJZgmDC00Rf12bioh',  # noqa
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)
