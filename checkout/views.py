from checkout.forms import OrderForm
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'strip_public_key': 'pk_test_51J8TH6JCvONQIszN8CmraPKb2feb0d8dbpiyyQVp04gdk4JAfOOobiXanmWd8o09EJV12hocqJbYhyJuzC43d3LC00VARaiq8D',
        'client_secret': 'sk_test_51J8TH6JCvONQIszNgQipsLbF2s8odxlRX0VyxG02nyVi2WvJyF0m3S1KaX6f6Nj6dXQaeoL4jN5a8WKkUyEMnKZ700GUbsnZrA'
    }

    return render(request, template, context)
        
    
