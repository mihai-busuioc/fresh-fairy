from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
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

    if item_id in list(cart.keys()):
        if date in cart[item_id]['items_by_date'].keys():
            cart[item_id]['items_by_date'][date] += quantity
        else:
            cart[item_id]['items_by_date'][date] = quantity
    else:
        cart[item_id] = {'items_by_date': {date: quantity}}

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the service in cart """

    quantity = int(request.POST.get('quantity'))
    date = None
    if 'your_date' in request.POST:
        date = request.POST['your_date']
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if quantity > 0:
            cart[item_id]['items_by_date'][date] = quantity
        else:
            del cart[item_id]['items_by_date'][date]
            if not cart[item_id]['items_by_date']:
                cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the service from cart """

    try:
        date = None
        if 'your_date' in request.POST:
            date = request.POST['your_date']
            cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            del cart[item_id]['items_by_date'][date]

            if not cart[item_id]['items_by_date']:
                cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
