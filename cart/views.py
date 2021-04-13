from django.shortcuts import render, redirect
from services.models import Services

# Create your views here.


def view_cart(request):
    """ A view to return the cart content page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add service to cart """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    date = None
    if 'your_date' in request.POST:
        date = request.POST['your_date']
    cart = request.session.get('cart', {})

    """if date:"""
    if item_id in list(cart.keys()):
        if date in cart[item_id]['items_by_date'].keys():
            cart[item_id]['items_by_date'][date] += quantity
        else:
            cart[item_id]['items_by_date'][date] = quantity
    else:
        cart[item_id] = {'items_by_date': {date: quantity}}
    """else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity"""

    request.session['cart'] = cart
    return redirect(redirect_url)
